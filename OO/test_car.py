from unittest import TestCase

from car import Motor


class CarTestCase(TestCase):

    def test_velocity(self):
        motor = Motor()
        self.assertEqual(0, motor.velocity)

    def test_speed_up(self):
        motor = Motor()
        motor.speed_up()
        self.assertEqual(1, motor.velocity)
