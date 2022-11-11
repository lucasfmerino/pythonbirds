class Motor:
    velocity = 0

    def __init__(self, acceleration=1):
        self.acceleration = acceleration

    def speed_up(self):
        self.velocity += self.acceleration
        return self.velocity

    def speed_down(self, down=2):
        self.velocity -= (down * self.acceleration)
        self.velocity = max(0, self.velocity)
        return self.velocity

    def show_speed(self):
        print(self.velocity)


class Direction:
    orientations = ['North ^', 'East >', 'South v', 'West <']

    def __init__(self, orientation=0):
        self.orientation = orientation

    def turn_right(self):
        self.orientation += 1
        if self.orientation > 3:
            self.orientation = 0
        return self.orientations[self.orientation]

    def turn_left(self):
        self.orientation -= 1
        if self.orientation < 0:
            self.orientation = 3
        return self.orientations[self.orientation]

    def show_direction(self):
        print(self.orientations[self.orientation])


class Car:
    def __init__(self, direction=Direction(), motor=Motor()):
        self.direction = direction
        self.motor = motor

    def velocity(self):
        return self.motor.velocity

    def speed_up(self):
        return self.motor.speed_up()

    def speed_down(self):
        return self.motor.speed_down()

    def dir(self):
        return self.direction.orientations[self.direction.orientation]

    def turn_right(self):
        return self.direction.turn_right()

    def turn_left(self):
        return self.direction.turn_left()


if __name__ == '__main__':
    car = Car()

    print(car.dir())
    print(car.velocity())

    print()
    print(car.speed_up())
    print(car.speed_up())
    print(car.speed_up())
    print(car.speed_up())
    print(car.speed_up())

    print()
    print(car.turn_left())
    print(car.turn_left())
    print(car.turn_left())
    print(car.turn_left())
    print(car.turn_left())
    print(car.turn_right())
    print(car.turn_right())
    print(car.turn_right())
    print(car.turn_right())
    print(car.turn_right())

    print()
    print(car.speed_down())
    print(car.speed_down())
    print(car.speed_down())
    print(car.speed_down())
