PACKNAME= xetzle00_xkozum08_xsimun04_xtoulm00
REPONAME= IVS_Projekt_2
all: compile

compile:
	@echo 'Python files do not need to be compiled.'

dependencies_python:
	sudo apt update
	sudo apt install python3.8
	sudo apt install -y python3-pip
	#installs pyqt5 and everything needed for it
	sudo apt-get install '^libxcb.*-dev' libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev libxkbcommon-dev libxkbcommon-x11-dev
	pip install pyqt5

dependencies_doxygen:
	sudo apt-get install doxygen

run: calc.py
	python3 $<

run_profile: standardDeviation.py
	python3 $<

test: test_calcMath.py
	python3 $<

profile: 
	@echo 'Python files do not need to be compiled.'

doc: Doxyfile
	doxygen $<

pack: clean Doxyfile
	rm -rf $(PACKNAME)
	mkdir ./$(PACKNAME)
	mkdir ./$(PACKNAME)/repo
	cd ../.. && cp -r ./$(REPONAME) $(REPONAME)_c
	mv ../../$(REPONAME)_c ./$(PACKNAME)/repo/$(REPONAME)
	rm -r ./$(PACKNAME)/repo/$(REPONAME)/src/$(PACKNAME)
	doxygen Doxyfile
	cp -r ./doc/ ./$(PACKNAME)
	mkdir ./$(PACKNAME)/install
	cp ../installer/setup.exe ./$(PACKNAME)/install/
	zip -r $(PACKNAME).zip $(PACKNAME)

clean:
	rm -rf doc
	rm -rf $(PACKNAME)
	rm -f warning_doxygen.txt