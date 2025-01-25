# Explanation
# Prototype Interface: Defines the clone method that must be implemented by any class that wants to allow cloning.
# Concrete Prototype (EnemyPrototype): Implements the clone method using copy.deepcopy to create a deep copy of the object.
# Client: Uses the prototype to create a clone and then customizes the cloned object as needed.
# In this example, the EnemyPrototype class is used to create prototypes for different types of enemies. The client_code function clones the prototype and customizes the cloned enemy. This pattern allows efficient creation of new enemies while ensuring they start with the same state as the prototype and can be easily customized afterward.

import copy
from abc import ABC, abstractmethod


class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass
    
    
class enemy(Prototype):
    def __init__(self, name, health, power):
        self.enemy_name = name
        self.health = health
        self.attack_power = power
        
    def clone(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        return f"Enemy name: {self.enemy_name}, health: {self.health}, attach power: {self.attack_power}"
    
    
class client:
    def client_code(self, prototype):
        clone1 = prototype.clone()
        print('Configuring clone 1')
        clone1.health = 90
        clone1.attack_power = 30
        print(clone1)
        
        clone2 = prototype.clone()
        print('Configuring clone 2')
        clone2.health = 95
        clone2.attack_power = 50
        print(clone2)
    
    
if __name__ == "__main__":
    main_prototype = enemy("Goblin", 100, 15)
    print('original enemy', main_prototype)
    
    client().client_code(main_prototype)