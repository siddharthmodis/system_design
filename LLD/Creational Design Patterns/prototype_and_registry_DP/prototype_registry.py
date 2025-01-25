import copy
from abc import ABC, abstractmethod


class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass
    
    
class Vehicle(Prototype):
    def __init__(self, car_type, car_name, car_color):
        self.car_type = car_type
        self.car_name = car_name
        self.car_color = car_color
        
    def clone(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        return f"Car type : {self.car_type}, car name: {self.car_name}, car color: {self.car_color}"
    
    
class PrototypeRegistry:
    registry = {}
    
    def register_prototype(self, name, prototype):
        if name not in PrototypeRegistry.registry:
            PrototypeRegistry.registry[name] = prototype
        else:
            raise ValueError('Prototype already exists.')
        
    def unregister_prototype(self, name):
        if name in PrototypeRegistry.registry:
            del PrototypeRegistry.registry[name]
        else:
            raise ValueError('Prototype does not exists for the name provided.')
        
    def get_prototype(self, name):
        if name in PrototypeRegistry.registry:
            prototype = PrototypeRegistry.registry[name]
            return prototype.clone()
        else:
            raise ValueError('Prototype does not exists for the name provided.')
        
        
if __name__ == "__main__":
    sedan_car = Vehicle('Toyota', 'Camry', 'White')
    suv_car = Vehicle('Tata', 'Tigor', 'Silver')
    pickup_truck = Vehicle('Mahindra', 'Pickup', 'White')
    
    
    proto_registry = PrototypeRegistry()
    proto_registry.register_prototype('sedan_car', sedan_car)
    proto_registry.register_prototype('suv_car', suv_car)
    proto_registry.register_prototype('pickup_truck', pickup_truck)
    
    # print(proto_registry.registry)
    
    cloned_sedan = proto_registry.get_prototype('sedan_car')
    cloned_suv = proto_registry.get_prototype('suv_car')
    
    print('Cloned vehicles before making any modification')
    print('Cloned sedan', cloned_sedan.car_type, cloned_sedan.car_name, cloned_sedan.car_color)
    print('Cloned sedan', cloned_suv.car_type, cloned_suv.car_name, cloned_suv.car_color)
    print('-----------------------')
    
    print('Cloned vehicales after modification')
    cloned_sedan.car_color = 'Black'
    cloned_suv.car_name = 'Curvv'
    print('Cloned sedan', cloned_sedan.car_type, cloned_sedan.car_name, cloned_sedan.car_color)
    print('Cloned sedan', cloned_suv.car_type, cloned_suv.car_name, cloned_suv.car_color)
    