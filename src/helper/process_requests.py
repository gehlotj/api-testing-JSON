import logging
import requests
logger = logging.getLogger(__name__)

class Req:

    """The following class is responsible for executing the action/methods on the given resource.
       Allowed actions are: GET,POST,PUT and DELETE
       FUNCTIONS
       ---------
       a) perform_operations(): Function will execute the actions
    """

    def __init__(self,method,url,header,data):
        self.__header = header
        self.__payload = data
        self.__url = url
        self.method = method

    def perform_operations(self):
        """The following function will execute the actions.
           Exception Caught: ConnectionError, HTTPError, ReadTimeout
        """
        logger.debug("Performing operation on %s with %s action",self.__url,self.method)
        try:
            if self.method == 'post' or self.method == 'POST':
                return requests.post(url = self.__url, headers = self.__header, data = self.__payload)
            if self.method == 'put' or self.method == 'PUT':
                return requests.put(url = self.__url, headers = self.__header, data = self.__payload)
            if self.method == 'get' or self.method == 'GET':
                return requests.get(url = self.__url, headers = self.__header, data = self.__payload)
            if self.method == 'delete' or self.method == 'DELETE':
                return requests.delete(url = self.__url, headers = self.__header, data = self.__payload)
            logger.error('Invalid method %s for %s',self.method,self.__url)
        except (requests.ConnectionError, requests.HTTPError, requests.ReadTimeout):
            logger.error('Unable to perform the action due to Connection error, server timeout or http error.Common Cause\
             \na)Check the Base URL value. \nb)Check your network connection')
        except Exception as error_exception:
            logger.error('Unknown error occured with exception %s',error_exception)
        return None
