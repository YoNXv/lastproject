from clint import Father


class seats(Father):
    def __init__(self, seat_id, availability: bool, place, id_bus):
        super().__init__(id_bus=id_bus)
        self.__seat_id=seat_id
        self.__availability=availability
        self.__place=place


    def set_seat_id(self, seat_id):
        self.__seat_id=seat_id
    def get_seat_id(self):
        return self.__seat_id


    def set_availability(self, availability):
        self.__availability = availability
    def get_availability(self):
        return self.__availability


    def set_place(self, place):
        self.__place=place
    def get_place(self):
        return self.__place



