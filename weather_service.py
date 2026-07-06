import requests
from config import API_KEY


def get_weather(city):
        
       
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    raise Exception("Bad request\nPlease check input")
                case 401:
                    raise Exception("Unauthorized User\nAPI key is invalid")
                case 403:
                    raise Exception("Forbidden\nAccess Denied")
                case 404:
                    raise Exception("Not found\nCity was not found")
                case 500:
                    raise Exception("Internal Server Error\nPlease try again later")
                case 502:
                    raise Exception("Bad Gateway\nInvalid response from server")
                case 503:
                    raise Exception("Service Unvailable\nServer is down, Please try again later")
                case 504:
                    raise Exception("Gateway Timeout\nServer response unavailable")
                case _:
                    raise Exception(f"Error Occured\n{http_error}")
        except requests.exceptions.ConnectionError:
            raise Exception("Connection Error:\nCheck Internet Connection")
        except requests.exceptions.Timeout:
            raise Exception("Timeout Error:\nServer has timed out")
        except requests.exceptions.TooManyRedirects:
            raise Exception("Too many Redirects:\nCheck URL")
        except requests.exceptions.RequestException as req_error:
            raise Exception(f"Request Error:\n{req_error}")