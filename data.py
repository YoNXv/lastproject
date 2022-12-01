from bus import bus
from seats import seats


class Op:
    bus_list:list[bus]=[bus("1","From Gaza to Hebron"),
                        bus("2","From Jerico to Akaa"),
                        bus("3","From Haifa to Jerusalem")
                        ]
    Seats_list:list[seats]=[seats(id_bus='1', seat_id="01" ,availability=True, place="First row in the right" ),
                            seats(id_bus='1', seat_id="02" ,availability=True, place="First row in the left"    ),
                            seats(id_bus='1', seat_id="03" ,availability=False,place="Second row in the right"   ),
                            seats(id_bus='1', seat_id="04" ,availability=True, place="Second row in the left"  ),
                            seats(id_bus='1', seat_id="05" ,availability=False,place="Third row in the middle"),

                            seats(id_bus='2', seat_id="01", availability=True, place="First row in the right"),
                            seats(id_bus='2', seat_id="02", availability=False, place="First row in the left"),
                            seats(id_bus='2', seat_id="03", availability=False, place="Second row in the right"),
                            seats(id_bus='2', seat_id="04", availability=False, place="Second row in the left"),
                            seats(id_bus='2', seat_id="05", availability=True, place="Third row in the middle"),

                            seats(id_bus='3', seat_id="01", availability=False, place="First row in the right"),
                            seats(id_bus='3', seat_id="02", availability=False, place="First row in the left"),
                            seats(id_bus='3', seat_id="03", availability=False, place="Second row in the right"),
                            seats(id_bus='3', seat_id="04", availability=True, place="Second row in the left"),
                            seats(id_bus='3', seat_id="05", availability=True, place="Third row in the middle")

                            ]
    def buses(self):
        for a in self.bus_list:
            print(a.get_id_bus(),a.get_location())

    def chosen(self,a):
        for i in self.bus_list:
            if i.get_id_bus()==a:
                for y in self.Seats_list:
                    if a==y.get_id_bus() and y.get_availability()==True:
                     print(y.get_seat_id(),y.get_place())

    def chosen_seat(self,T):
        for i in self.Seats_list:
            if i.get_seat_id()==T:
                i.set_availability(False)
        print('your seat booked successfully')

    @staticmethod
    def check_input_is_empty(*input):
        for item in input:
            if item.isspace() or item == "":
                print("empty input")
                exit()
            else:
                pass

    def check_id_bus(self,a):
        for i in self.bus_list:
            if int(i.get_id_bus())==int(a):
                return True
        else:
            print("Erorr")
            exit()

    def check_id_seat(self,T,a):
        for i in self.Seats_list:
            if int(i.get_seat_id())==int(T) and i.get_id_bus()==a and i.get_availability()==True:
                return True
            elif int(i.get_seat_id())==int(T) and i.get_id_bus()==a and i.get_availability()==False:
                print( "this seat is booked")
                exit()
        else:
            print("Erorr")
            exit()





