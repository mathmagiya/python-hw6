from abc import ABC, abstractmethod
import itertools
#--
class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

class Vending(IVending):
    def __init__(self,jsonMachine):
        self.id = jsonMachine["id"]
        self.model = jsonMachine["model"]
        self.cash= jsonMachine["money"]
        self.capacity= jsonMachine["capacity"]
        self.status = jsonMachine["status"]
        self.offerings =[[ Product(p["name"],p["price"]) for i in range(p["quantity"])] for p in jsonMachine["items"]]
        self.offerings = list(itertools.chain(*self.offerings))

    def addItems(self, p:Product):
        if len(self.offerings)== self.capacity:
            raise ValueError('The machine is full')
        self.offerings.append(p)
    def purchaseProduct(self,p:Product,payment:float):
        try:
            idx =  self.offerings.index(p)
            if self.offerings[idx].price > payment:
                raise ValueError(f'The price of the product is:{self.offerings[idx].price}')
            if payment - self.offerings[idx].price > self.cash:
                raise ValueError('There is not enough cash')
            self.cash= self.cash + self.offerings[idx].price - payment
            self.offerings.pop(idx)
        except:
            raise ValueError('There is not this product in the machine')
    def addCash(self, newCash):
        self.cash = self.cash + newCash
