class Item:
    def __init__(self,value,weight):
        self.value=value
        self.weight=weight
        self.ratio=value/weight
        
def frac_knap(capacity,items):
    items.sort(key=lambda x:x.ratio,reverse=True)
    
    total_value=0
    for item in items:
        if capacity==0:
            break
        
        take_weight=min(capacity,item.weight)
        total_value+=take_weight*item.ratio
        capacity-=take_weight
        
    return total_value

n=int(input("Enter the no. of items : "))
items=[]
for i in range(n):
    value=float(input("Enter the value of the item : "))
    weight=float(input("Enter the weight of the item : "))
    
    items.append(Item(value,weight))
    
capacity=float(input("Enter the capacity of the Knapsack : "))

max_value=frac_knap(capacity,items)
print(max_value)