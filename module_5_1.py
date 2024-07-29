# Задача "Developer - не только разработчик"- решение:
class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.nFloors = number_of_floors

    def go_to(self, new_floor: int):
        if new_floor < self.nFloors:


            for f in range(1, new_floor+1):

                print(f)

def main():
    # №1

    h1 = House('ЖК Горский', 18)
    h2 = House('Домик в деревне', 2)

    h1.go_to(5)
    h2.go_to(10)

    print('Такого этажа не существует!')

if __name__ == '__main__':
    main()






