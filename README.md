# Project Description :
The api-testing-JSON module is designed to simplify the REST API testing process using pytest. The whole process can be set up by configuring a single JSON file. The program reads the required parameters defined in the definition file and perform operations and tests the endpoints. The testing on each endpoint is validated by the status code.

### Advantages :
  - End user needs to define all the test urls and their endpoint objects under one file and the program takes care of the testing operations against the defined status code
  - Supports token authentications
  - Easy to manage and can be incorporated with CI/CD

### Functionality :
  - Supports ordering, so the endpoint tests executes in a certain order
  - Output from one endpoint can be used later as a input for the other endpoint payload

### Installation Instructions :
  - Download the package and add it to your existing project
  - Edit the api-testing-JSON/src/config/definition.json file
  - Execute the following command:
  ```pytest . ```

### Operations Allowed :
  - GET, POST, PUT and DELETE

### JSON object definitions and requirements :

* **header (required)**
    * Header definitions
* **token (optional)**
    * Token to authenticate the request
* **base_url (required)**
    * Base url of the resources
* **order (optional)**
    * Determines the order in which the endpoints tests has to be run.
* **endpoints: (required)**
    * **valid identifier (required)**
        * String value to identify the end point  
    * **resource (required)**
        * Resource identifier
    * **method (required)**
        * Allowed methods (GET,PUT,POST,DELETE)
    * **data (required)**
        * Payload needed to fulfill the requests
    * **status_code (required)**
        * The status code on which the endpoint perform the test
    * **input (optional)**
        * The following attribute when set to true will trigger the program to save the result retrieved from a GET request. This result data can be used later in the program as input parameters for other endpoint payload requests. For further explanation please refer to example2.json located under src/config. Endpoint id 2 exhibit the functionality described above.
    * **update (optional)**
        * The following attribute will require the valid identifieralong with a list of parameter that needs to be updated from the value stored previously in 'input' section. For further explanation please refer to example2.json located under src/config. Endpoint id 2 exhibit the functionality described above.

### FAQ:

- How to change the log level to produce debug information?
- Update the value of log level in file src/helper/__init__.py from logging.INFO to logging.DEBUG


Example 1:
``` json
{
   "header":{
      "Content-Type":"application/json"
   },
   "order":[
      "1"
   ],
   "base_url":"https://mynewassettmanager.com/Dev/",
   "endpoints":{
      "1":{
         "resource":"assign-request",
         "method":"GET",
         "data":"",
         "status_code":200
      }
   }
}
