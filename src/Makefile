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
