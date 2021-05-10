import json
import urllib.parse
import pytest
from src.helper.process_requests import Req




class TestEndpoints:
    """Testing the endpoints
    """

    def validate_endpoint_info(self,endpoint,log):
        """The following function will lookup for all the required parameters in
           the endpoint defination needed to process the endpoint.
        """
        valid_params = ['method','resource','data','status_code']
        result = all(map(lambda param: True if param in list(endpoint.keys()) else False,valid_params))
        if not result:
            log.error("One of the required filed in missing in following endpoint defination.\
            \nRequired fileds are: method, resource, data\
            \nEndppoint: {0}".format(endpoint))
        return result


    def update(self,update_values,data,result,log):
        """The following function will update the current data values by replacing
           them with previously captured data values
        """
        for index,content in update_values.items():
            if index in result:
                for value in content:
                    if value in data:
                        data[value] = result[index]['result'][0][value]
                    else: log.warning("Unable to find the {0} in {1}".format(value,data))
        return data


    def process(self,order,endpoints):
        """The following function will process all the endpoitns giving the first precendence to
           the order.
        """
        if order and endpoints:
            for seq in order:
                if seq in endpoints:
                    yield endpoints[seq],seq
                    del endpoints[seq]
        for seq,_ in endpoints.items():
            yield endpoints[seq],seq


    def test_endpoints(self,order,endpoints,base_url,header,log):
        """The following function is responsible for evaluting and executing all the endpoints.
           The function will evaluate the "update" and "input" functionality from the endpoints
           and take required actions.
        """
        endpoint_index_collection = {}
        for endpoint_info,sequence in self.process(order,endpoints):
            if not self.validate_endpoint_info(endpoint_info,log):
                pytest.fail()
            method = endpoint_info['method']
            url = urllib.parse.urljoin(base_url,endpoint_info['resource'])
            data = endpoint_info['data']

            #the following statement updates the data with a previous index value
            if 'update' in endpoint_info:
                data = self.update(endpoint_info["update"],data,endpoint_index_collection,log)

            result = Req(method,url,header,json.dumps(data)).perform_operations()
            log.info("Testing: {0} for method {1}\nResponse: {2}".format(url,method,result.status_code))
            log.debug("Testing: {0} for method {1} and data {2}\nResponse: {3}".format(url,method,data,result.text))
            assert endpoint_info['status_code'] == result.status_code

            #the following statement stores the return data in case if it needs to be used by any other resource later in the test
            if 'input' in endpoint_info:
                if method == 'GET':
                    try:
                        endpoint_index_collection[sequence] = result.json()
                    except Exception as exception_result:
                        log.warning("Cannot save the endpoint index data for index {0}. Exception: {1}".format(sequence,exception_result))
                else:
                    log.error("Cannot use input on {0} method".format(method))
