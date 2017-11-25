wrapper for Adafruit's [MAX9744 amplifier python library](https://github.com/adafruit/Adafruit_Python_MAX9744)

## install notes

#### *MAX9744 amp library and dependencies*
```
sudo apt-get install python3-smbus
git clone https://github.com/adafruit/Adafruit_Python_MAX9744.git
cd Adafruit_Python_MAX9744
sudo python3 setup.py install
```
enable I2C in raspi-config
```
sudo raspi-config
```

set pi's system volume to 97% (0db)
```
amixer set PCM -- 97%
```

#### *pygame and dependencies*
```
sudo apt-get install libsdl-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev
sudo apt-get install libsmpeg-dev libportmidi-dev libavformat-dev libswscale-dev
sudo pip3 install pygame
```
[reference](https://www.raspberrypi.org/forums/viewtopic.php?f=32&t=33157&p=332140&hilit=croston%2bpygame#p284266)

\- or - (untested)

```
sudo apt-get install python3-pygame
```
