CC=python -m nuitka

linux:
	pyside6-project build
	$(CC) --show-progress  --include-data-dir=data=data --include-data-dir=resources=resources --assume-yes-for-downloads --onefile --plugin-enable=pyside6 NUSGet.py -o NUSGet

linux-install:
	install -d /opt/NUSGet
	install NUSGet /opt/NUSGet/
	install ./packaging/icon.png /opt/NUSGet/NUSGet.png
	install ./packaging/NUSGet.desktop /usr/share/applications

clean:
	rm NUSGet
	rm -rd NUSGet.build/
	rm -rd NUSGet.dist/
	rm -rd NUSGet.onefile-build/
