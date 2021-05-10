"""The following module will read and validate the definition file
"""
import json
import sys
import logging
from os import path
logger = logging.getLogger(__name__)



class GatherData:
    """The following class is responsible for gathering the data from definition file
        validating it and returning the needed parameters
        FUNCTIONS
        ---------
        a) get_endpoints() : Return all the endpoints
        b) get_header() : Return the header definition
        c) get_order() : Return the list of order if the user prefer to run the
           tests in a certain order
        d) get_base_url() : Return the base url of the resource thats being tested
        e) get_data() : Return the data if validation is succesful. Otherwise terminate the program
        f) get_token() : Return the token from the definition file
        g) get_logger() : Return the reference to the logger
        h) validate_json() : Validate the JSON file for any syntax error
        i) validate_attr() : Validate the required attribute from the definition file
    """

    BASE_DIR    = path.abspath('.')
    JSON_LOC    = 'src/config/'
    JSON_FILE   = 'definition.json'
    CONFIG_FILE = path.join(BASE_DIR,JSON_LOC,JSON_FILE)


    def __init__(self):
        self.__data = self.get_data()


    def get_endpoints(self):
        """Return all the endpoints defined in the definition file
        """
        if 'endpoints' in self.__data:
            return self.__data['endpoints']


    def get_header(self,token=None):
        """Return the header definition from the definition file
        """
        if 'header' in self.__data:
            if token:
                self.__data['header']['Authorization'] = '\n'.join(token).replace('\n','')
            return self.__data['header']


    def get_token(self):
        """Return the token value from the definition file
        """
        if 'token' in self.__data:
            return self.__data['token']


    def get_order(self):
        """Return the order list from the definition file
        """
        if 'order' in self.__data:
            return self.__data['order']


    def get_base_url(self):
        """Return the base_url from the input definition file
        """
        if 'base_url' in self.__data:
            return self.__data['base_url']


    def get_data(self):
        """Function to retrieve the data if attribute and file validation passes.
           On failure to pass both the validation test the function can cause
           fatal error and terminate
           **SYS.EXIT**
        """
        data = GatherData.validate_json(GatherData.CONFIG_FILE)
        if data and GatherData.validate_attr(data):
            return data
        logger.error('Unable to process the definition data. Please review the logs')
        sys.exit(1)


    def get_logger(self):
        """The following function will return the ref of logging module
        """
        return logging

    @staticmethod
    def validate_json(file_location):
        """Functions to make sure the file has valid JSON content
        """
        try:
            data = None
            with open(file_location) as file_cursor:
                data = json.load(file_cursor)
            logger.debug(data)
            return data
        except FileNotFoundError :
            logger.error('Unable to locate the file. Looking at location: %s',file_location)
        except json.JSONDecodeError:
            logger.error('Invalid JSON File')
        except Exception as error_desc:
            logger.error('Unknown error occured while loading the file at location: \
            %s\nError: %s',file_location,error_desc)
        return None

    @staticmethod
    def validate_attr(data):
        """Function to verify if all the required attributes are available to execute the tests
        """
        attributes = ['base_url','header','endpoints']
        for attr in attributes:
            if attr not in data:
                logger.error("Unable to find the attribute %s in definition file", attr)
                return False
        return True
