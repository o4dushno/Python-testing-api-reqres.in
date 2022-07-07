from payloads import register_request_valid, register_response_valid, register_request_invalid
from test_login import random_email, random_password
from config import MAIN_URL
import requests
import pytest
import json


@pytest.mark.register
class TestRegistration:
    url = MAIN_URL + '/api/register/'
    
    @pytest.mark.smoke
    def test_register_with_valid_data(self):
        """ Регистрация с валидными данными """
        response = requests.post(self.url, data=register_request_valid)
        assert response.status_code == 200, f"Error: got status code {response.status_code} instead of 200"
        assert json.loads(response.text) == register_response_valid


    @pytest.mark.smoke
    @pytest.mark.parametrize("test_data", register_request_invalid)
    def test_register_with_invalid_data(self, test_data):
        """ Регистрация с неправильными данными """
        response = requests.post(self.url, data=test_data)
        response_data = json.loads(response.text)
        
        if test_data in register_request_invalid[3:6:2]:
            pytest.xfail(f"Expected bug with next data --> {test_data}")
            
        assert response.status_code == 400, f"This invalid data was processed as valid: {test_data}"
        assert "token" not in response_data, f"Token was received with the following incorrect data {test_data}"
        assert "id" not in response_data, f"ID was received with the following incorrect data {test_data}"


    @pytest.mark.repeat(10)
    def test_registration_random_data(self):
        data = {
            "email": random_email(),
            "password": random_password()
        }
        response = requests.post(self.url, data=data)
        response_cleaned = json.loads(response.text)
        assert response.status_code == 400, f"This invalid data was processed as valid: {data}"
        assert "id" not in response_cleaned, f"ID was received with the following incorrect data {data}"
        assert "token" not in response_cleaned, f"Token was received with the following incorrect data {data}"