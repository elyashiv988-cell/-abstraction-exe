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
    def __init__(self):
        self.name = "WalkingDelivery"
    def deliver(self, order_id):
        print(f"Order {order_id} delivered by walking.")
    def get_eta(self):
        return 60

class ExpressDelivery(DeliveryMethod):
    def __init__(self):
        self.name = "ExpressDelivery"
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
print(f"Faster option: {faster_delivery.name}")

# 8 

class Notifier(ABC):
    @abstractmethod
    def send(self, recipient, message):
        pass

class PushNotifier(Notifier):
    def send(self, recipient, message):
        print(f"Push to {recipient}: {message}")

class WhatsAppNotifier(Notifier):
    def send(self, recipient, message):
        print(f"WhatsApp to {recipient}: {message}")

class InAppNotifier(Notifier):
    def send(self, recipient, message):
        print(f"In-app banner for {recipient}: {message}")

n1 =PushNotifier()
n2 =WhatsAppNotifier()
n3= InAppNotifier()

notifiers = [n1, n2, n3]

for n in notifiers:
    n.send("customer_42", "Your order is on the way!")

# 9 

class Restaurant(ABC):
    @abstractmethod
    def get_menu(self):
        pass
    @abstractmethod
    def prepare_order(self, item_name):
        pass

class ItalianRestaurant(Restaurant):
    def get_menu(self):
        return ['pasta', 'pizza', "tiramisu"]
    def prepare_order(self, item_name):
        print(f"Cooking {item_name} with olive oil!")

class SushiRestaurant(Restaurant):
    def get_menu(self):
        return ["maki", "nigiri", 'ramen']
    def prepare_order(self, item_name):
        print(f"Making fresh {item_name} with rice")

class BurgerJoint(Restaurant):
    def get_menu(self):
        return ['burger', 'fries', 'shake']
    def prepare_order(self, item_name):
        print(f"Grilling {item_name} on the fire")

resturants=[ItalianRestaurant(), SushiRestaurant(), BurgerJoint()]

for r in resturants:
    print(r.get_menu())
    items = r.get_menu()
    r.prepare_order(items[0])

# 10

class DeliveryMethod(ABC):
    @abstractmethod
    def deliver(self, order_id):
        pass
    @abstractmethod
    def get_eta(self):
        pass
    @abstractmethod
    def get_cost(self, distance_km):
        pass

class BikeDelivery(DeliveryMethod):
    def __init__(self):
        self.name="BikeDelivery"
    def deliver(self, order_id):
        print(f"Delivering order {order_id} by bike.")
    def get_eta(self):
        return 25
    def get_cost(self, distance_km):
        return distance_km * 2.5

class DroneDelivery(DeliveryMethod):
    def __init__(self):
        self.name="DroneDelivery"
    def deliver(self, order_id):
        print(f"Flying order {order_id} with a drone.")
    def get_eta(self):
        return 8
    def get_cost(self, distance_km):
        return 30.0

class CarDelivery(DeliveryMethod):
    def __init__(self):
        self.name = "CarDelivery"
    def deliver(self, order_id):
        print(f"Driving order {order_id} by car.")
    def get_eta(self):
        return 15
    def get_cost(self, distance_km):
        return 12.0 + (distance_km * 1.5)

class WalkingDelivery(DeliveryMethod):
    def __init__(self):
        self.name = "WalkingDelivery"
    def deliver(self, order_id):
        print(f"Walking order {order_id} to destination.")
    def get_eta(self):
        return 50
    def get_cost(self, distance_km):
        return 0.0

class Platform:
    def __init__(self):
        self.methods=[BikeDelivery(), DroneDelivery(), CarDelivery(), WalkingDelivery()]
    def cheapest_option(self, distance_km):
        cheapest = self.methods[0]
        for method in self.methods:
            if method.get_cost(distance_km) < cheapest.get_cost(distance_km):
                cheapest = method
        return cheapest
    def fastest_option(self):
        fastest = self.methods[0]
        for m in self.methods:
            if m.get_eta() < fastest.get_eta():
                fastest=m
        return fastest

platfrom = Platform()
cheapest = platfrom.cheapest_option(5.0)
fastest = platfrom.fastest_option()
print(f"Cheapest: {cheapest.name}")
print(f"Fastest: {fastest.name}")
