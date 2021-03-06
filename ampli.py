#!/usr/bin/python3
# MAX9744 library wrapper
# 9/7/17
# updated: 11/24/17

import time
from Adafruit_MAX9744 import MAX9744


class Ampli(object):
    '''
    wrapper for adafruit's MAX9744 library

    contains following methods:
    set_volume(), increase_volume(), decrease_volume()
    if controlling more than one amp from a single pi, must change
    the i2c address on the amp itself and pass in new address to MAX9744()
    more here: https://github.com/adafruit/Adafruit_Python_MAX9744

    NOTE: calls to the MAX9744 module when no amp is connected results in the following error:
    OSError: [Errno 121] Remote I/O error
    '''

    def __init__(self, volume=16):
        self.min = 0
        self.max = 63
        self.volume = volume
        self.unmute_volume = self.volume
        
        try:
            self.amp = MAX9744()
            self.set_volume(self.volume)
        except OSError:
            print("\ngot an OSError when instantiating the amp, check that it's connected and make sure I2C is enabled")
            time.sleep(5)
            print('reraising exception...')
            time.sleep(2)
            raise

    def _constrain(self, value):
        '''constrain input values to valid range of 0-63 inclusive'''
        cnstrnd = self.min if value < self.min else self.max if value > self.max else value

        if cnstrnd != value:
            print('received value of {} outside valid range of 0-63'.format(value))
            print('constraining to {}'.format(cnstrnd))

        return cnstrnd

    def get_volume(self):
        print('volume currently set to {}'.format(self.volume))

        return self.volume

    def set_volume(self, value, suppress=False):
        '''suppress keyword argument used to silence redundant print statements when muting'''
        value = self._constrain(value)

        if not suppress:
            print('setting volume to {}...'.format(value))

        self.amp.set_volume(value)
        self.volume = value

    def decrease_volume(self):
        self.amp.decrease_volume()
        self.volume -= 1
        print('decreased volume by one step to {}'.format(self.volume))

    def increase_volume(self):
        self.amp.increase_volume()
        self.volume += 1
        print('increased volume by one step to {}'.format(self.volume))

    def mute(self):
        '''mute amp and store last volume for unmuting'''
        print('muting amp')
        self.unmute_volume = self.volume
        self.set_volume(self.min, suppress=True)

    def unmute(self):
        print('unmuting amp')
        self.set_volume(self.unmute_volume, suppress=True)

    def ramp_to(self, value):
        '''
        ramp from current volume to input value by one step in one second increments.
        use Ctrl-C to interrupt the process and leave volume set to the current step
        '''
        direction = None
        target = self._constrain(value)

        if target == self.volume:
            print('volume already set to {}'.format(target))
            return
        elif target > self.volume:
            direction = 1
            interval = target - self.volume
        elif target < self.volume:
            direction = -1
            interval = self.volume - target

        try:
            print('ramping volume from {} to {} in 1 second increments'.format(self.volume, target))
            step = self.volume

            for i in range(interval):
                step += direction
                self.set_volume(step)
                time.sleep(1)
        except KeyboardInterrupt:
            print('\nuser interrupt received')
            print('leaving volume set to {}'.format(self.volume))
