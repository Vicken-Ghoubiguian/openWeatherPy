# Definition of the Error class...
class Error:

    #
    def __init__(self, code, message):

        self.__cod = code
        self.__message = message

    #
    def getCode(self):

        return self.__cod

    #
    def getMessage(self):

        return self.__message