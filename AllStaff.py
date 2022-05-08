from abc import ABC, abstractmethod

class Vending(ABC):
    @abstractmethod
    def addItems(self, Product):
        if len(self.offerings)== self.capacity:
            raise ValueError('The machine is full')
        self.offerings.append(p)
    @abstractmethod
    def purchaseProduct(self,Product,payment:float):
    
    @abstractmethod
    def addCash(self, newCash):
        pass
