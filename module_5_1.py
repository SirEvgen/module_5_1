class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if new_floor > self.number_of_floors or new_floor == 0:
            print(f"\033[3m\033[1:31m Такого этажа в доме {self.name} нет \033[0m")
        else:
            self.number_of_floors = self.new_floor
            print(f'\033[3m\033[1;36m Название: {self.name}, этаж: {self.number_of_floors} \033[0m')


h1 = House("ЖК Эверест", 20)
h2 = House("Теремок", 1)
h3 = House('ЖК Мегаизба', 15)
h1.go_to(17)
h2.go_to(2)
h3.go_to(11)
