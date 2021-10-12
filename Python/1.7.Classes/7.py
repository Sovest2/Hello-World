# class Class_name:
# description


class Airplane:
    '''Класс создания самолета'''

    def __init__(self, seats, engines):
        self.seats = seats
        self.engines = engines

    def make_noise(self):
        'Делает шум. Однострочное описание'
        print('Уровень шума среднего реактивного самолета - 130-140 децибел.')

    def fly(self, time):
        '''
        Заставляет самолет летать.
        Многострочное описание
        '''
        print(f'Вжжуууух, и вы в Турции. Время в пути: {time} минут')


# airbus = Airplane(253, 2)
# print(f'Кол-во мест: {airbus.seats} \nКол-во двигателей: {airbus.engines}')
# airbus.fly(85)
# print(Airplane.__doc__)
# print(Airplane.make_noise.__doc__)
# print(Airplane.fly.__doc__)

# boeing_777 = Airplane(400, 2)
# print(f'Кол-во мест: {boeing_777.seats} \nКол-во двигателей: {boeing_777.engines}')
# boeing_777.fly(98)

# an_225 = Airplane(6, 6)
# print(f'Кол-во мест: {an_225.seats} \nКол-во двигателей: {an_225.engines}')
# an_225.fly(110)


class Transport:
    """Класс для создания разных типов транспорта"""

    def __init__(self, type_of_trans, wheels, passengers, num_of_passengers, v_gas, v_gas_now):
        self.type_of_trans = type_of_trans
        self.wheels = wheels
        self.passengers = passengers
        self.num_of_people = num_of_passengers
        self.v_gas = v_gas
        self.v_gas_now = v_gas_now
        self.consumption = 4

    def beep(self):
        print('Бииииииип!')

    def move(self):
        if self.type_of_trans == 'bus':
            self.consumption += 30
        if self.num_of_people > 10:
            self.consumption += 5
        elif self.consumption > 20:
            self.consumption += 10

        self.v_gas_now -= self.consumption

        if self.v_gas_now < 0:
            self.v_gas_now = 0
        print(f'У вас осталось топлива: {self.v_gas_now} л.')

    def check_gas(self):
        print(
            f'Уровень топлива: {self.v_gas_now}. Объем бензобака: {self.v_gas}.'
        )

    def refill(self):
        while self.v_gas_now < self.v_gas:
            self.v_gas_now += 1
            print(f'Бак заполнен на: {self.v_gas_now} л')
        print('Бак полностью заправлен.')

# Наследование
class Car(Transport):
    def __init__(self, type_of_trans, wheels, passengers, num_of_passengers, v_gas, v_gas_now, owner):
        super().__init__(type_of_trans, wheels, passengers,
                         num_of_passengers, v_gas, v_gas_now)
        self.owner = owner
        self.wheels = 4

    def say_owner(self):
        print(f'Владелец авто: {self.owner}')

# autobus = Transport(type_of_trans='bus', wheels=6, passengers=40,
#         num_of_passengers=27, v_gas=80, v_gas_now=54)
# autobus.beep()
# autobus.check_gas()
# autobus.refill()
# autobus.move()

# volkswagen = Transport(type_of_trans='car', wheels=4, passengers=3, num_of_passengers=3, v_gas=40, v_gas_now=20)
# volkswagen.beep()
# while volkswagen.v_gas_now > 0:
#     volkswagen.move()
# volkswagen.refill()
# print()

# audi = Car('car',4, 3, 3, 40, 30, 'Пастернак Б.Л.')
# audi.say_owner()
# audi.beep()
# audi.check_gas()
# while audi.v_gas_now > 0:
#     audi.move()
# audi.refill()

# print()


# Инкапсуляция
class Kettle:
    def turn_on(self):
        print('нажали кнопку')
        self.__boil()
        self.__check_temperature()
        self.__beep()
        self._turn_off()

    def __boil(self):
        print('Подогрев воды')

    def __check_temperature(self):
        print('Проверка температуры воды')

    def __beep(self):
        print('Подача звукового сигнала')

    def _turn_off(self):
        print('Автоматическое выключение')


# new_kettle = Kettle()
# new_kettle.__boil()
# new_kettle.__check_temperature()
# new_kettle.turn_on()
# new_kettle._turn_off()
# new_kettle._Kettle__boil()

# Полиморфизм
# def func(x, y):
#     return x + y

# print(func(15, 20))
# print(func('15', '20'))
# print(func([15], [20]))


# class Animal:
#     legs = 4
#     tail = 1

#     def voice(self):
#         print('Какой-то непонятный звук')

# class Cat(Animal):
#     def voice(self):
#         print('Не правильно ты бутерброд ешь, колбасой вниз надо. ')

# class Dog(Animal):
#     def voice(self):
#         print('Сам ты балбес')

# cat1, cat2 = Cat(), Cat()
# dog1, dog2 = Dog(), Dog()

# ktulhu = Animal()

# farm_band = [cat1, cat2, dog1, dog2, ktulhu]

# for i in farm_band:
#     i.voice()

# for i in farm_band:
#     if isinstance(i, Cat):
#         i.cat_voice()
#     if isinstance(i, Dog):
#         i.dog_voice()




# Задача 3. Джун
class Human:
    def __init__(self, name):
        self.name = name

    def answer_question(self, question):
        print('Очень интересный вопрос! Не знаю.')


class Student(Human):
    def __init__(self, name):
        super().__init__(name)

    def ask_question(self, someone, question):
        print(f'{someone.name}, {question}')
        someone.answer_question(question)
        print()

class Mentor(Human):
    def __init__(self, name):
        super().__init__(name)

    def answer_question(self, question):
        if 'проект' in question:
            print('Люблю такие вопросы. Сейчас расскажу.')
        elif 'груст' in question:
            print('Отдохни. А потом возвращайся с вопросами по проекту.')
        else:
            super().answer_question(question)


class HR(Human):
    def __init__(self, name):
        super().__init__(name)

    def answer_question(self, question):
        if 'груст' in question:
            print('Попей чаечку. Хочешь видео с котиками?')
        elif 'отпуск' in question:
            print('Когда-нибудь - точно.')
        elif 'зарплата' in question:
            print('Печеньки - на кухне. Чаек там же.')
        else:
            super().answer_question(question)

student = Student('Виталик')
mentor = Mentor('Олег')
hr = HR('Настя')

student.ask_question(mentor, 'когда зарплата?')
student.ask_question(hr, 'Когда зарплата?')
student.ask_question(mentor, 'мне грустно, что делать?')
student.ask_question(hr, 'мне грустно, что делать?')
student.ask_question(mentor, 'что не так с моим проектом?')
student.ask_question(hr, 'что не так с моим проектом?')
student.ask_question(mentor, 'когда отпуск?')
student.ask_question(hr, 'когда отпуск?')