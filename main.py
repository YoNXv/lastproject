from clint import Father
from bus import bus
from data import Op
from seats import seats
print('Welcome in our buses company')
x=Op()
x.buses()
a=input("choose the bus you want:")
print("                                                   "
      ""
      ""
      "")

x.check_input_is_empty(a)
x.check_id_bus(a)
x.chosen(a)
print("       \n         ")
 
 


T=input("book your seat:")
x.check_input_is_empty(T)
x.check_id_seat(T,a)
x.chosen_seat(T)


