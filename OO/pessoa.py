class Pessoa:
    eyes = 2

    def __init__(self, *sons, name=None, age=0):
        self.name = name
        self.age = age
        self.sons = list(sons)

    def cumprimentar(self):
        return f'Hello! I am {self.name}.'

    @staticmethod
    def breathe():
        return True

    @classmethod
    def cls_names_attributes(cls):
        return f'{cls} - ayes: {cls.eyes}'


class Homem(Pessoa):

    def cumprimentar(self):
        pessoa_cumprimentar = super().cumprimentar()
        return f'{pessoa_cumprimentar} "Aperto de Mão".'


class Alien(Homem):
    eyes = 3

    def cumprimentar(self):
        return f'kadagaraf nokyud {self.name} nokyud.'


if __name__ == '__main__':

    arthur = Pessoa(name='Arthur')
    lucas = Homem(arthur, name='Lucas', age=31)

    for son in lucas.sons:
        print(son.name)

    print()
    print(lucas.cumprimentar())
    print(arthur.cumprimentar())

    print()
    arthur.lastname = 'Merino'
    print(arthur.lastname)
    lucas.weight = 80
    print(lucas.weight)
    del lucas.weight

    print()
    print(lucas.__dict__)
    print(arthur.__dict__)

    print()
    print(Pessoa.breathe())

    print()
    print(Pessoa.cls_names_attributes())
    print(lucas.cls_names_attributes())

    print()
    print(isinstance(lucas, Pessoa))
    print(isinstance(lucas, Homem))
    print(isinstance(arthur, Pessoa))
    print(isinstance(arthur, Homem))

    print()
    alien = Alien(name='Zur')

    print(alien.cls_names_attributes())
    print(alien.cumprimentar())
