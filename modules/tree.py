# "modules/tree.py", licensed under the MIT license
# Copyright 2024-2025 NinjaCheetah

from modules.core import TitleData
from PySide6.QtCore import QAbstractItemModel, QModelIndex, Qt, QSortFilterProxyModel
from PySide6.QtGui import QIcon


class TreeItem:
    def __init__(self, data, parent=None, metadata=None):
        self.data = data
        self.parent = parent
        self.children = []
        self.metadata = metadata

    def add_child(self, item):
        self.children.append(item)

    def child(self, row):
        return self.children[row]

    def child_count(self):
        return len(self.children)

    def column_count(self):
        return len(self.data)

    def data_at(self, column):
        if 0 <= column < len(self.data):
            return self.data[column]
        return None

    def row(self):
        if self.parent:
            return self.parent.children.index(self)
        return 0


class NUSGetTreeModel(QAbstractItemModel):
    def __init__(self, data, parent=None, root_name=""):
        super().__init__(parent)
        self.root_item = TreeItem([root_name])
        self.setup_model_data(data, self.root_item)

    def setup_model_data(self, title, parent):
        if isinstance(title, dict):
            for key, value in title.items():
                if isinstance(value, list):
                    key_item = TreeItem([key, ""], parent)
                    parent.add_child(key_item)
                    for entry in value:
                        tid = entry.get("TID")
                        name = entry.get("Name")
                        versions = entry.get("Versions", {})
                        if tid:
                            tid_item = TreeItem([f"{tid} - {name}", ""], key_item, entry.get("Ticket"))
                            key_item.add_child(tid_item)
                            for region, version_list in versions.items():
                                region_item = TreeItem([region, ""], tid_item)
                                tid_item.add_child(region_item)
                                for version in version_list:
                                    danger = entry.get("Danger") if entry.get("Danger") is not None else ""
                                    archive_name = (entry.get("Archive Name") if entry.get("Archive Name") is not None
                                                    else entry.get("Name").replace(" ", "-"))
                                    metadata = TitleData(entry.get("TID"), entry.get("Name"), archive_name,
                                                         version, entry.get("Ticket"), region, key, danger)
                                    public_versions = entry.get("Public Versions")
                                    if public_versions is not None:
                                        try:
                                            public_ver = public_versions[str(version)]
                                            version_str = f"v{version} ({public_ver})"
                                        except KeyError:
                                            version_str = f"v{version}"
                                    else:
                                        version_str = f"v{version}"
                                    version_item = TreeItem([version_str, ""], region_item, metadata)
                                    region_item.add_child(version_item)

    def rowCount(self, parent=QModelIndex()):
        if parent.isValid():
            parent_item = parent.internalPointer()
        else:
            parent_item = self.root_item
        return parent_item.child_count()

    def columnCount(self, parent=QModelIndex()):
        return self.root_item.column_count()

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        item = index.internalPointer()

        if role == Qt.DisplayRole:
            item = index.internalPointer()
            return item.data_at(index.column())

        if role == Qt.DecorationRole and index.column() == 0:
            # Check for icons based on the "Ticket" metadata only at the TID level
            if item.metadata is not None and isinstance(item.metadata, bool):
                if item.metadata is True:
                    return QIcon.fromTheme("dialog-ok")
                else:
                    return QIcon.fromTheme("dialog-cancel")
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.root_item.data_at(section)
        return None

    def index(self, row, column, parent=QModelIndex()):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()

        if not parent.isValid():
            parent_item = self.root_item
        else:
            parent_item = parent.internalPointer()

        child_item = parent_item.child(row)
        if child_item:
            return self.createIndex(row, column, child_item)
        return QModelIndex()

    def parent(self, index):
        if not index.isValid():
            return QModelIndex()

        child_item = index.internalPointer()
        parent_item = child_item.parent

        if parent_item == self.root_item:
            return QModelIndex()

        return self.createIndex(parent_item.row(), 0, parent_item)

class TIDFilterProxyModel(QSortFilterProxyModel):
    def filterAcceptsRow(self, source_row, source_parent):
        source_model = self.sourceModel()
        index = source_model.index(source_row, 0, source_parent)
        item = index.internalPointer()

        filter_text = self.filterRegularExpression().pattern().lower()
        # If the item matches what the user searched for.
        if item and filter_text in item.data_at(0).lower():
            return True
        # Check if children match, though I don't think this matters because the children of a title will always just
        # be regions.
        for i in range(source_model.rowCount(index)):
            if self.filterAcceptsRow(i, index):
                return True
        # Keep the regions and versions under those for any titles that matched, so you can actually download from the
        # search results.
        parent_item = index.parent().internalPointer() if index.parent().isValid() else None
        if parent_item and filter_text in parent_item.data_at(0).lower():
            return True
        else:
            grandparent_item = index.parent().parent().internalPointer() if index.parent().parent().isValid() else None
            if grandparent_item and filter_text in grandparent_item.data_at(0).lower():
                return True
        return False
