class Car():

    def __init__(self, id, model, year, engine, cost, mileage, updated_at):

        self.id = id
        self.model = model
        self.year = year
        self.engine = engine
        self.cost = cost
        self.mileage = mileage
        self.wheels = 4
        self.updated_at = updated_at


    def description_car(self):
        description = self.model + ' модель автомобиля, ' + self.year + ' года выпуска, с объёмом двигателя ' + self.engine + 'л, цена авто - ' + self.cost + 'и пробегом - ', self.mileage
        print('Представлен автомобиль на рынке: ' + description)
        print('Информация обновлена - ' + self.update_at)


    def get_id(self):
        print('Внутренний id автомобиля - ' + self.id)



    def get_model(self):
        print('Модель автомобиля - ' + self.model)


    def get_year(self):
        print('Год выпуска авто - ' + self.year)


    def get_engine(self):
        print('Объём двигателя автомобиля - ' + self.engine)


    def get_cost(self):
        print('Цена автомобиля - ' + self.cost)


    def get_mileage(self):
        print('Пробег авто - ' + self.mileage)


    def get_wheels(self):
        print('Автомобиль имеет ' + self.wheels + 'колёс.')


    def get_updated_at(self):
        print('Последние изменения по данному автомобилю - ' + self.updated_at)


    def update_model(self, text):
        self.model = text


    def update_year(self, num):
        self.year = num


    def update_engine(self, num):
        self.engine = num


    def update_cost(self, num):
        self.cost = num


    def update_mileage(self, num):
        self.mileage = num


    def update_wheels(self, num):
        self.wheels = num


    def set_updated_at(self, date):
        self.updated_at = date


    def compare(self, other):
        print(f'Модель: {self.model} vs {other.model}')
        print(f'Год выпуска: {self.year} vs {other.year}')
        print(f'Объём двигателя: {self.engine} vs {other.engine}')
        print(f'Цена: {self.cost} vs {other.cost}')
        print(f'Пробег: {self.mileage} vs {other.mileage}')
        print(f'Количество колёс: {self.wheels} vs {other.wheels}')
        print(f'Информация по первому товару изменялась - {self.updated_at}')
        print(f'Информация по второму товару изменялась - {other.updated_at}')
