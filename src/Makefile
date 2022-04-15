all: dependencies

dependencies:
	sudo apt update
	sudo apt install python3.8
	sudo apt install -y python3-pip
	#installs pyqt5 and everything needed for it
	sudo apt-get install '^libxcb.*-dev' libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev libxkbcommon-dev libxkbcommon-x11-dev
	pip install pyqt5
run: 
	python3 calc.py

test:
	python3 calcMathTests.py #change filename

profile:
	python3 profile.py
