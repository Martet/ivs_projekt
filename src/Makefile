out=xdoupo00_xlipta04_xvopal04_xzmitk01

all: dist/gui

dist/gui: gui.py NumberSystems.py mathLib.py
	pyinstaller -F -i "logo.png" --add-data "res/:res/" gui.py

kalkulacka_1.0-1_all.deb: dist/gui
	mkdir -p kalkulacka_1.0-1_all/usr/local/bin
	cp dist/gui kalkulacka_1.0-1_all/usr/local/bin/kalkulacka
	dpkg-deb --build --root-owner-group kalkulacka_1.0-1_all

pack: kalkulacka_1.0-1_all.deb clean
	rm -rf ../$(out) ../$(out).zip
	mkdir ../$(out)
	mkdir ../$(out)/doc
	mkdir ../$(out)/install
	mkdir ../$(out)/repo
	cp kalkulacka_1.0-1_all.deb ../$(out)/install
	rsync -a --exclude ../$(out) --exclude kalkulacka_1.0-1_all.deb .. ../$(out)/repo
	rm -rf ../$(out)/repo/$(out) ../$(out)/repo/src/kalkulacka_1.0-1_all/usr/local/bin/*
	zip -r ../$(out).zip ../$(out)
	rm -rf ../$(out)

run: dist/gui
	./dist/gui

test: test.py
	python3 test.py

profile: profiling.py
	seq 1 10000 | python3 profiling.py

clean:
	rm -rf build dist *.spec __pycache__

.PHONY: all clean test profile run pack
