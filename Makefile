linux:
	pyside6-project build
	nuitka3 --show-progress  --include-data-dir=data=data --include-data-dir=resources=resources --assume-yes-for-downloads --onefile --plugin-enable=pyside6 NUSGet.py

clean:
	rm NUSGet.bin
	rm -rd NUSGet.build/
	rm -rd NUSGet.dist/
	rm -rd NUSGet.onefile-build/
