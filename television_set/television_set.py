class TelevisionSet:

    def __init__(self):
        self._isOn = False
        self.channel: int = 1
        self.volume_level = 0

    def get_isOn(self):
        return self._isOn

    def turnOn(self):
        self._isOn = True

    def turnOff(self):
        self._isOn = False

    def setChannel(self, channel):
        if self.turnOn():
            self.channel = channel
        if 2 <= channel or channel <= 10:
            self.channel = channel
        else:
            raise ValueError('Tv Channel must be turned on')

    def getChannel(self):
        return self._channel

    def setVolumeLevel(self, volume):
        if self.turnOn():
            self.volume = volume
        if 1 <= volume or volume <= 100:
            self._volume_level = volume
        else:
            raise ValueError('Tv Channel Volume must be turned on.')

    def getVolumeLevel(self):
        return self._volume_level

    def channel_up(self):
        if self.turnOn() and self._channel <= 100:
            self.channel = +1
        self._channel = self._channel

    def channel_down(self):
        if self.turnOn() and self._channel >= 100:
            self.channel = -1
            self._channel = self._channel

    def volume_up(self):
        if self._volume_level <= 100:
            self.volume = +1
            self._volume_level = self._volume_level

    def volume_down(self):
        if self._volume_level <= 100:
            self.volume = -1
            self._volume_level = self._volume_level