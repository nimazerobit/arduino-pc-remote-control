# Arduino PC Remote Control

Control your PC with infrared remote control using Arduino

## Installation

1. Clone the repository:
	```
	git clone https://github.com/nimazerobit/arduino-pc-remote-control.git
	cd arduino-pc-remote-control
	```
	
2. Set up the Arduino:
-   Connect your Arduino to your PC.
-   Open  `arduino-source.ino` in Arduino IDE
-   Install IRRemote library ([V2.6.0](https://downloads.arduino.cc/libraries/github.com/z3t0/IRremote-2.6.0.zip))
-   Modify `#define  RECEIVER_PIN  4` if you don't want to use pin 4 for your infrared receiver
-   Upload sketch to your Arduino

3. Install the required Python packages:
   `pip install -r requirements.txt`

4. Run python script
	`python main.py`

## Usage

1. Create remote control json file with `remote_code_extarctor.py`
	Use `Remote Code Receiver 2` in menu

2. Modify actions of buttons by editing exported json file
	All actions [here](#actions)

3. Create or modify .env file
	```
	ARDUINO_PORT = COM3
	BAUD_RATE = 9600
	VERSION = 1.0.0
	REMOTE_MAP_FILE = example_remote.json
	```

4. Run main script
	`python main.py`

## Actions

- Play and Pause Media -> `PLAY_PAUSE`
- Next Media -> `NEXT_TRACK`
- Previous Media -> `PREVIOUS_TRACK`
- Volume Up -> `VOLUME_UP`
- Volume Down -> `VOLUME_DOWN`
- Volume Mute -> `VOLUME_MUTE`
- New virtual desktop -> `ADD_DESKTOP`
- Switch to desktop -> `SWITCH_DESKTOP_{NUM}`
	- Start from 1 (`SWITCH_DESKTOP_1`)
- Shutdown -> `SHUTDOWN`
- Lock -> `LOCK`
- Function Buttons -> `F_BUTTON_{NUM}`
	- From 1 to 24 (`F_BUTTON_1`)
