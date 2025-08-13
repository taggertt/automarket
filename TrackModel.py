from CarModel import Car

class Track(Car):

    def __init__(self, id, model, year, engine, cost, mileage, updated_at):
        super().__init__(id, model, year, engine, cost, mileage, updated_at)
        self.wheels = 8


    def description_track(self):
        description = self.model + ' модель грузовика, ' + self.year + ' года выпуска, с объёмом двигателя ' + self.engine + 'л, цена авто - ' + self.cost + 'и пробегом - ', self.mileage
        print('Представлен автомобиль на рынке: ' + description)
        print('Информация обновлена - ' + self.update_at)


