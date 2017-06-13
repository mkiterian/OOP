import unittest

from computer import Computer
from computer import Laptop
from computer import CellPhone
from computer import SmartPhone

class OOPTest(unittest.TestCase):
	''' OOP Tests for Data Abstraction, Encapsulation, Method Overriding
		Inheritance and Polymorhism
	'''
	def setUp(self):
		self.comp = Computer('Dell', 16, 2000, 'Windows 7')
		self.lappy = Laptop('HP', 4, 1000, 'Ubuntu', 4)
		self.smartphone = SmartPhone('iPhone', '2GB', '16GB', 'iOS 11', '7', '4G')
		self.cell = CellPhone('Tecno', 'T100', '3G')

	def test_comp_instance_property_is_set(self):
		self.assertEqual(self.comp.memory_size, 16)

	def test_cell_is_instance_of_cellphone(self):
		self.assertIsInstance(self.cell, CellPhone)

	def test_laptop_is_computer_child(self):
		self.assertIsInstance(self.lappy, Computer)

	def test_laptop_overrides_power_up_from_computer(self):
		self.assertEqual(self.lappy.power_up(), 'The Laptop is booting')

	def test_warranty_property_is_hidden(self):
		with self.assertRaises(AttributeError, msg='to access warranty use get_warranty'):
			self.comp.__warranty

	def test_laptop_obj_is_laptop_and_is_computer(self):
		self.assertIsInstance(self.lappy, (Computer, Laptop))

	def test_smartphone_is_computer(self):
		self.assertIsInstance(self.smartphone, Computer)

	def test_smartphone_is_cellphone(self):
		self.assertIsInstance(self.smartphone, CellPhone)

	def test_smartphone_is_computer_and_cellphone(self):
		self.assertIsInstance(self.smartphone, (Computer, CellPhone))

if __name__ == '__main__':
	unittest.main()

