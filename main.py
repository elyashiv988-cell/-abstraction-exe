from abc import ABC , abstractmethod

# 1

class DeliveryMethod(ABC):
    
    @abstractmethod
    def deliver(self,order_id):
        pass
    
class BikeDelivery(DeliveryMethod):

    def deliver(self, order_id):
        return f"Order {order_id} delivered bt bike" 

bike_delivery = BikeDelivery()
print(bike_delivery.deliver(101))       

# 2 

class DeliveryMethod(ABC):
    @abstractmethod
    def deliver(self,order_id):
        pass
    
class DroneDelivery(DeliveryMethod):
    
    def deliver(self, order_id):
        return f"Order {order_id} dropped by drone at your door."
    
class CarDelivery(DeliveryMethod):
    
    def deliver(self, order_id):
        return f"Order {order_id} brought to your building by car."
    
drone = DroneDelivery()
car = CarDelivery()

print(drone.deliver(202))
print(car.deliver(202))
