# pytest -v --tb=line
# -s to show print
from payloads import login_request_valid, login_response_valid, login_request_invalid
from config import MAIN_URL
import pytest
import requests
import json
import random
import string


def random_email():
    half = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(1, 50)))
    return half + "@gmail.com"

def random_password():
    return ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(1, 50)))


@pytest.mark.login
class TestLogin:
    """ Тестирование авторизации """
    
    url = MAIN_URL + "/api/login/"
    
    @pytest.mark.smoke
    def test_login(self):
        """ Авторизция с валидными данными """
        response = requests.post(self.url, data=login_request_valid)
        assert response.status_code == 200, f"Error: got status code {response.status_code} instead of 200"
        assert json.loads(response.text) == login_response_valid
    
    
    @pytest.mark.smoke
    @pytest.mark.parametrize("test_data", login_request_invalid)
    def test_login_bad_data(self, test_data):
        """ Авторизация с невалидными данными """
        response = requests.post(self.url, data=test_data)
        if test_data in login_request_invalid[3:6:2]:
            pytest.xfail("Expected bug")
        assert response.status_code == 400, f"This invalid data was processed as valid: {test_data}"
        assert json.loads(response.text) != login_response_valid, f"A token was obtained using the following data {test_data}"
    
    
    @pytest.mark.repeat(10)
    def test_login_random_data(self):
        data = {
            "email": random_email(),
            "password": random_password()
        }
        
        response = requests.post(self.url, data=data)
        assert response.status_code == 400, f"This invalid data was processed as valid: {data}"
        assert json.loads(response.text) != login_response_valid, f"A token was obtained using the following data {data}"