# Create-A-Show

Welcome! For my final project, I decided  [Check it out in action.](https://www.youtube.com/watch?v=6sI_j_qrEh0).

![Create-A-Show](IMG_1913.jpeg) 

## Setup 

### Necessary Hardware
- Raspberry Pi
- Momentary push button (soldered) x4
- ESP32
- 3.7v LiPo Battery
- Various ribbon cables
- Keyboard
- Mouse
- Monitor w/ sound or speakers

### Hardware Setup

Here is a hookup guide of the electronics for the main box:
![Here is an approximate hookup guide](tv_hookup.png) 

And here is a hookup of the electronics for the "remote". Note that I used an ESP32 and a vibration sensor instead of the Arduino and the accelerometer:
![Here is an approximate hookup guide](remote_hookup_bb.png) 

Here's a picture of the actual setup of both:
![Actual](IMG_1939.jpeg)

![Actual](IMG_1931.jpeg)

#### Main Box Wiring:

##### Button 1 (Mutes the music)
- GND: Connected to GPIO pin 6 (GND)
- DO: Connected to the Raspberry Pi GPIO pin 11 (BCM 17)

##### Button 2 (Switches the music) 
- GND: Connected to GPIO pin 25 (GND)
- DO: Connected to the Raspberry Pi GPIO pin 22 (BCM 25)

##### Button 3 (Mutes the video audio) 
- GND: Connected to GPIO pin 34 (GND)
- DO: Connected to the Raspberry Pi GPIO pin 31 (BCM 6)

##### Button 4 (Switches the currently playing video) 
- GND: Connected to GPIO pin 39 (GND)
- DO: Connected to the Raspberry Pi GPIO pin 37 (BCM 26)

#### Remote Wiring:

#### LiPo Battery
- GND: Connected to a GND on the ESP32

#### The Printer Itself
In order to create the printer itself, see [the documentation on Brachio Graph](https://brachiograph.readthedocs.io/en/latest/)

### Software to Install 

### Processing
Download Processing [here](https://processing.org/)

#### BrachioGraph
Again, check out the [Brachio Graph documentation](https://brachiograph.readthedocs.io/en/latest/). You can also simply `pip install -r requirements.txt`, we have all the necessary requirements on there.  

In order to re-create our work one would need: A Raspberry Pi 3 B+, four servo motors, three popsicle sticks, two binder clips (one small and one large), a breadboard, a switch, access to Python, and access to processing.

### Running it
1. Connect the Raspberry Pi to a monitor, keyboard, and mouse (or use a remote desktop like VNC Viewer).
2. On a terminal, run `sudo pigpiod`, then navigate to the repo. Run `cd BrachioGraph` and then run `python3 controller.py`. This will set the printer up and make it ready to receive an image to print.
2. Open the Processing sketch underneath `BrachioGraph/DrawSomethingKeys`
3. Draw something! 
4. Hit `s` to save the drawing.
5. Hit the push button! 
6. Now we wait - hitting the push button tells the Pi to convert the image you just saved into a JSON file. This can take anywhere from 1-3 minutes. After it's created, it takes another 2-7 minutes for the Servo Scribbler to complete the drawing.
7. Enjoy!
