wrapper for Adafruit's [MAX9744 amplifier python library](https://github.com/adafruit/Adafruit_Python_MAX9744)

adds the following methods:
```
get_volume()
set_volume(value)  # automatically constrains input value to 0-63 inclusive
decrease_volume()  # lowers volume by one step
increase_volume()  # raises volume by one step
ramp_to()          # raise or lower volume one step per second, ctl-C to stop
mute()
unmute()
```

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
