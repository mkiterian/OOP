class Computer():

    def __init__(self, brand, memory_size, storage_size, os_type):
        self.brand = brand
        self.memory_size = memory_size
        self.storage_size = storage_size
        self.os_type = os_type
        #use name mangling to make it private
        self.__warranty = 12

    def power_up(self):
        return 'The Computer is booting'

    def shutdown(self):
        return 'The computer is shutting down'

    def show_spec(self):
        print('Brand: {} Memory: {} GB Storage Size: {} GB'.format(
            self.brand, self.memory_size, self.storage_size))

    def set_warranty(self, months):
        self.__warranty = months

    def get_warranty(self, elapsed_months=0):
        self.__warranty -= elapsed_months
        return self.__warranty