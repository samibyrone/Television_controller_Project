import unittest

from television_set.television_set import TelevisionSet


class TestMyTelevision(unittest.TestCase):

    def test_for_television_to_be_off(self):
        television_set = TelevisionSet()
        self.assertFalse(television_set.turnOff())

    def test_for_television_be_on(self):
        television_set = TelevisionSet()
        self.assertFalse(television_set.turnOff())
        tele = television_set._isOn
        self.assertEqual(television_set.turnOn(), tele)

    def test_for_television_can_set_channel(self):
        television_set = TelevisionSet()
        self.assertFalse(television_set.turnOff())
        tele = television_set.turnOn()
        self.assertEqual(television_set.turnOn(), tele)
        channel = 1
        self.assertEqual(television_set.getChannel(), channel)
        display = television_set.setChannel(10)
        self.assertEqual(television_set.setChannel(10), display)

    def test_for_television_can_set_volume(self):
        television_set = TelevisionSet()
        self.assertFalse(television_set.turnOff())
        tele = television_set.turnOn()
        self.assertEqual(television_set.turnOn(), tele)
        channel = 1
        self.assertEqual(television_set.getChannel(), channel)
        display = television_set.setChannel(10)
        self.assertEqual(television_set.setChannel(10), display)
        sound = 1
        self.assertEqual(television_set.getVolumeLevel(), sound)
        sound = television_set.setVolumeLevel(20)
        self.assertEqual(television_set.setVolumeLevel(20), sound)


