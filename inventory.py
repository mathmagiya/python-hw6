import json
from Vending import Vending
import math

class Inventory:
    def __init__(self):
        self.load_machines()

    def load_machines(self):
        with open('initialinventory.json', "r") as read_file:
            self.machines = [Vending(m) for m in json.load(read_file)['machines']]

    def get_min_cash(self):
        m_with_less_cash = min([m for m in self.machines if m.status=='active'], key= lambda m: m.cash)
        return m_with_less_cash
    def greater_cash(self,idx_a, idx_b):
        return self.machines[idx_a].cash > self.machines[idx_b].cash

    def union_items(self,idx_a,idx_b):
        items = list()
        items.extend(self.machines[idx_a].offerings)
        items.extend(self.machines[idx_b].offerings)
        return items
    def intersection_items(self,idx_a,idx_b):
        items = [a for a in self.machines[idx_a].offerings if self.find_item(a, self.machines[idx_b].offerings)]
        return items
    def find_item(self,product,list_products):
        for element in list_products:
            if element.name == product.name:
                return True
        else:
            return False
    def difference_items(self,idx_a,idx_b):
        items = [a for a in self.machines[idx_a].offerings if not self.find_item(a, self.machines[idx_b].offerings)]
        return items

    def difference_cash(self, idx_a, idx_b):
        return math.abs(self.machines[idx_a].cash - self.machines[idx_b].cash)
