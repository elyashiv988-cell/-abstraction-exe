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

# 3 

class DeliveryMethod(ABC):
    def __init__(self,company_name):
        self.company_name=company_name
    @abstractmethod
    def deliver(self,order_id):
            pass
class BikeDelivery(DeliveryMethod):
    def __init__(self, company_name):
        super().__init__(company_name)
    def deliver(self, order_id):
        return f"[{self.company_name}] Order {order_id} - bike_delivery"

class DroneDelivery(DeliveryMethod):
    def __init__(self, company_name):
        super().__init__(company_name)
    def deliver(self, order_id):
        return f"[{self.company_name}] Order {order_id} - bike_delivery"
    
bike=BikeDelivery("SpeedRiders")
print(bike.deliver(303))
drone=DroneDelivery("SkyEx")
print(drone.deliver(303))

# 4 

class DeliveryMethod(ABC):

    @abstractmethod
    def deliver(self,order_id):
            pass
    @ abstractmethod
    def get_eta(self):
        pass
class BikeDelivery(DeliveryMethod):
    
    def deliver(self, order_id):
        return f"Order {order_id} delivered by bike."
    def get_eta(self):
        return 30
class DroneDelivery(DeliveryMethod):
    
    def deliver(self, order_id):
        return f"Order {order_id} delivered by drone"
    def get_eta(self):
        return 15
bike = BikeDelivery()
print(bike.deliver(1))
print(f"ETA: {bike.get_eta()} minutes\n")

drone = DroneDelivery()
print(drone.deliver(2))
print(f"ETA: {drone.get_eta()} minutes")

# 5 

class DeliveryMethod(ABC):
    @abstractmethod
    def deliver(self, order_id):
        pass

class BrokenDelivery(DeliveryMethod):
    def deliver(self, order_id):
        pass

delivery_service = BrokenDelivery()
print("(after fix) No error.")
    


   
# 6 

class DeliveryFee:
    @staticmethod
    def calculate(distance_km,rate_per_km):
        return distance_km * rate_per_km

    @staticmethod
    def with_surcharge(base_fee, surcharge_percent):
        return base_fee * (1 + surcharge_percent / 100)

    @staticmethod
    def is_free(distance_km):
        return distance_km <= 2.0

fee = DeliveryFee.calculate(5, 3.0)
final_fee = DeliveryFee.with_surcharge(15.0, 10)
free_delivery = DeliveryFee.is_free(1.5)

print(f"{fee} / {final_fee} / {free_delivery}")

# 7

class DeliveryMethod(ABC):
    @abstractmethod
    def deliver(self, order_id):
        pass
    @abstractmethod
    def get_eta(self):
        pass

class WalkingDelivery(DeliveryMethod):
    def deliver(self, order_id):
        print(f"Order {order_id} delivered by walking.")
    def get_eta(self):
        return 60

class ExpressDelivery(DeliveryMethod):
    def deliver(self, order_id):
        print(f"Order {order_id} delivered by express.")
    def get_eta(self):
        return 10

class DeliveryHelper:
    @staticmethod
    def faster(d1,d2):
        if d1.get_eta() < d2.get_eta():
            return d1
        return d2

walker = WalkingDelivery()
express = ExpressDelivery()

faster_delivery = DeliveryHelper.faster(walker, express)
print(f"Faster option: {faster_delivery.__class__.__name__}")