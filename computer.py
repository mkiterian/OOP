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

class Laptop(Computer):
    def __init__(self, brand, memory_size, storage_size, os_type, battery_life):
        super().__init__(brand, memory_size, storage_size, os_type)
        self.battery_life = battery_life

    def show_battery_life(self):
        return 'The battery lasts up to {} Hours'.format(self.battery_life)

    def can_run_windows_ten(self):
        if self.memory_size > 1 and self.storage_size > 100:
            if self.os_type != 'Windows 10':
                return True
            else:
                return False
        return False

    def power_up(self):
        return 'The Laptop is booting'

    def shutdown(self):
        return 'The Laptop is shutting down'

    def install_drivers(self):
        return 'Drivers are being installed'

class CellPhone():    
    def __init__(self, brand, model, sim_type):
        self.brand = brand
        self.model = model
        self.sim_type = sim_type
        self.contacts = {}

    def add_contact(self, name, number):
        self.name = name
        self.number = number
        self.contacts[self.name] = self.number

    def call(self, name):
        if name in self.contacts.keys():
            return 'Calling {}'.format(name)

class SmartPhone(Computer, CellPhone):
    def __init__(self, brand, memory_size, storage_size, os_type, model, sim_type):
        Computer.__init__(self, brand, memory_size, storage_size, os_type)
        CellPhone.__init__(self, brand, model, sim_type)