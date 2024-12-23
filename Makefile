CC=python -m nuitka
ARCH_FLAGS?=

all:
	python build_translations.py
	$(CC) --show-progress --assume-yes-for-downloads NUSGet.py $(ARCH_FLAGS) -o NUSGet

install:
	rm -rd /opt/NUSGet/
	install -d /opt/NUSGet
	cp -r ./NUSGet.dist/* /opt/NUSGet/
	chmod 755 /opt/NUSGet/
	install ./packaging/icon.png /opt/NUSGet/NUSGet.png
	install ./packaging/NUSGet.desktop /usr/share/applications

clean:
	rm NUSGet
	rm -rd NUSGet.build/
	rm -rd NUSGet.dist/
	rm -rd NUSGet.onefile-build/
