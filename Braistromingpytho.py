print(True==1)  # that's give True a outuput 
print("\n")
print(True+1)
print("Diffrence between shallow and deep copy ","\n")
# .copy() create just a shallow copy : 
x=[[1,2]]
y=x.copy()
print(x[0],y[0]) # that's mean x[0] and y[0] point to the same memory object , wich is the inner list [1,2]
y[0].append(3) 
print(x)   # Most poeple that will give [[1,2]] , but the real output is [[1,2,3]] 

# use the .deepcopy() method to create a real separated copy of the x list : 
import copy
h=[[1,2,3]]
z=copy.deepcopy(h)
z[0].append(4)
print(h)  #return just [[1,2,3]] indpendt from the deep copy z
print(z)

print("\n")

# In python : Same Value==equal in python !! 

print(10==10.0)
 # in other languages , 
print("\n")
print(10 == 10.0)          # True (same value)
print(type(10) == type(10.0))  # False (different types) int vs float
# print(10 is 10.0)          # False (different objects)

def add_item(item,my_list=[]):
    my_list.append(item)
    return my_list

print(add_item(1))
print(add_item(2))
print(add_item(3))

print("also fot sert  keeps growing across calls : \n")

def add_set(item,my_set=set()):
    my_set.add(item)
    return my_set


print(add_set(1))
print(add_set(2))
print(add_set(3))

print("If you want a fresh list each time, use None as the default and create a new list inside:\n")

def add_item_2(my_item,my_list=None):
    if my_list==None:
        my_list=[]
    my_list.append(my_item)
    return my_list

print(add_item_2(4))
print(add_item_2(5))


print("Global vs Local variable :\n") 
x=10 # global variabl
def change(x):
    x = 20  # Local variable, shadows the global one
    # This assignment only affects the local scope
change(x)
print(x)  # Still 10

print("\n")

y=20
def show():
    print(y)
show()
print(y)
