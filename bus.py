from clint import Father


class bus(Father):
    def __init__(self, id_bus, location):
        super().__init__(id_bus=id_bus)
        self.__location=location

    def get_location(self):
        return self.__location
    def set_location(self, location):
        self.__location=location








