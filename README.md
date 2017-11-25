wrapper for Adafruit's MAX9744 amplifier python library

## install notes

#### *MAX9744 amp library and dependencies*
```
sudo apt-get install python3-smbus
git clone https://github.com/adafruit/Adafruit_Python_MAX9744.git
cd Adafruit_Python_MAX9744
sudo python3 setup.py install
```
enable I2C in raspi-config
set pi's system volume to 100%
```
amixer set PCM -- 100%
```
