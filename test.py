# Import the main module to use: the OpenPyther one...
import openPyther.openPyther as openPyther

#
import sys

# Initialization of the 'openPyther' object with the wished localisation, the wished country code and the OpenWeather API key as parameters...
openPytherObject = openPyther.OpenPyther("", "", "")

# Display the 'openPyther' object as a string...
print(openPytherObject)
