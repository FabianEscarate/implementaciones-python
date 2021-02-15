import requests
import json

class DigiAPI:

    def __init__(self, dict_api_config):
        _url = dict_api_config['URL'] if 'URL' in dict_api_config else None 
        if _url is None:
            Exception('No Existe configuracion de API')
        else:
            self.__private_url_api = _url

    def get_digi(self, arg_element):
        result = {}
        n_elements = 0
        value_error = False
        try:
            if arg_element == 'all':
                n_elements = -1
            else:
                n_elements = int(arg_element)                    
        except ValueError as _ex:
            value_error = True

        if value_error:
            result = {
                "success": False,
                "message" : "Invalid value, can't convert str to int"
            }
        else:
            response = requests.get(self.__private_url_api)
            if response.status_code != 200:
                result = {
                    "success": False,
                    "message" : 'Status {0}, {1}'.format(response.status_code, response.text())
                }
            else:
                data = list(response.json())
                data = list(data[:n_elements]) if n_elements > -1 else data
                result = {
                    "success": True,
                    "data": data
                }
            
        return result