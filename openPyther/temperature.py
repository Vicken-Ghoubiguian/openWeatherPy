#
from . import temperatureEnum

# Definition of the Temperature class...
class Temperature:

	# Definition of the Temperature class constructor...
	def __init__(self, value):

		self.__value = value
		self.__measureUnit = temperatureEnum.TemperatureEnum.KELVIN

	#
	def getValue(self):

		return self.__value

	#
	def getMeasureUnit(self):

		return self.__measureUnit

	#
	def __getSymbolUnit(self):

		#
		if self.__measureUnit == temperatureEnum.TemperatureEnum.KELVIN:

			return "K"

		#
		elif self.__measureUnit == temperatureEnum.TemperatureEnum.CELSIUS:

			return "°C"

		#
		else:

			return "°F"

	#
	def __getMeasureUnitAsString(self):

		#
		if self.__measureUnit == temperatureEnum.TemperatureEnum.KELVIN:

			return "Kelvin"

		#
		elif self.__measureUnit == temperatureEnum.TemperatureEnum.CELSIUS:

			return "Celsius"

		#
		else:

			return "Fahrenheit"

	#
	def setTemperatureAsKelvin(self):

		print("Conversion in Kelvin...")

	#
	def setTemperatureAsCelsius(self):

		print("Conversion in Celsius...")

	#
	def setTemperatureAsFahrenheit(self):

		print("Conversion in Fahrenheit...")
	
	#
	def __str__(self):

		return self.__value + " " + self.__getSymbolUnit() + " (" + self.__getMeasureUnitAsString() + ")"