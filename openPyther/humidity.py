# Definition of the Humidity class...
class Humidity:

	# Definition of the GeographicLocation class constructor...
	def __init__(self, value):

		self.__value = value
		self.__unitOfMeasure = "%"

	#
	def getValue(self):

		return self.__value

	#
	def getUnitOfMeasure(self):

		return self.__unitOfMeasure

	# Definition of the __str__ method to display the current object as a string...
	def __str__(self):
		
		return "{} {}".format(str(self.__value), str(self.__unitOfMeasure))