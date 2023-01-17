from abc import ABCMeta, abstractmethod
from datetime import datetime
import math


class Calculator(metaclass=ABCMeta):
    @abstractmethod
    def calulate_devery_fee(self, app, data):
        pass

class SimpleCalculator(Calculator):
    def calulate_devery_fee(self, app, data):
        try:
            cart_value = data["cart_value"]
            delivery_distance = data["delivery_distance"]
            number_of_items = data["number_of_items"]
            time = datetime.strptime(data["time"], '%Y-%m-%dT%H:%M:%SZ')

            if cart_value >= 100 * 100:
                # 100$, the delivery is free
                return 0

            delivery_fee = 0
            surcharge_cart_value = 0
            if cart_value < 1000:
                surcharge_cart_value = 1000 - cart_value
            delivery_fee += surcharge_cart_value

            charge_distance = 0
            # distance
            if delivery_distance <= 1000:
                charge_distance = 200
            else:
                charge_distance = 200 + math.ceil((delivery_distance - 1000) / 500) * 100
            delivery_fee += charge_distance

            # items
            charge_items = 0
            if number_of_items >= 5 and number_of_items <= 12:
                charge_items = (number_of_items - 4) * 50
            elif number_of_items > 12:
                charge_items = 50 * (13 - 4) + 120
            delivery_fee += charge_items

            if time.isoweekday() == 5 and time.hour >= 15 and time.hour <= 19:
                delivery_fee = delivery_fee*1.2

            if delivery_fee > 15 * 100:
                delivery_fee = 15 * 100

            return delivery_fee
        except Exception as e:
            app.logger.error(e)
            return -1

class Strategy:
    def __init__(self, calculator):
        self.calculator = calculator

    def get_results(self, app, data):
        return self.calculator.calulate_devery_fee(app, data)