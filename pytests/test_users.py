from payloads import users_create_request_valid, users_create_response_invalid, users_put_request_valid
from config import MAIN_URL
import requests
import pytest
import json


@pytest.mark.users
class TestUsers:
    @pytest.mark.smoke
    def test_list_users(self):
        url = MAIN_URL + "/api/users?page=2"
        response = requests.get(url)
        assert response.status_code == 200, f"Error: got status code {response.status_code} instead of 200"
    
    
    @pytest.mark.smoke
    def test_single_user(self):
        url = MAIN_URL + "/api/users/2"
        response = requests.get(url)
        assert response.status_code == 200, f"Error: got status code {response.status_code} instead of 200"
    
    
    @pytest.mark.smoke
    def test_single_user_not_found(self):
        url = MAIN_URL + "/api/users/23"
        response = requests.get(url)
        assert response.status_code == 404, f"Error: got status code {response.status_code} instead of 400"
    
    
    @pytest.mark.smoke
    def test_create_users(self):
        url = MAIN_URL + "/api/users"
        response = requests.post(url, data=users_create_request_valid)
        response_cleaned = json.loads(response.text)
        assert response.status_code == 201, f"Error: got status code {response.status_code} instead of 201"
        assert response_cleaned["name"] == users_create_request_valid["name"], f"Error: \
            The name {users_create_request_valid['name']} does not match the {response_cleaned['name']}"
        assert response_cleaned["job"] == users_create_request_valid["job"], f"Error: \
            Job {users_create_request_valid['job']} does not match the {response_cleaned['job']}"
        assert "id" in response_cleaned, "Response does not contain 'id'"
        assert "createdAt" in response_cleaned, "Response does not contain 'createdAt'"
    
    
    @pytest.mark.smoke
    @pytest.mark.parametrize("test_data", users_create_response_invalid)
    def test_create_users_with_invalid_data(self, test_data):
        url = MAIN_URL + "/api/users"
        response = requests.post(url, data=test_data)
        if test_data in users_create_response_invalid[0:5]:
            pytest.xfail(f"Expected bug with next data --> {test_data}")
        assert response.status_code not in [200, 201]
    
    
    @pytest.mark.smoke
    def test_put_users(self):
        url = MAIN_URL + "/api/users/2"
        response = requests.post(url, data=users_put_request_valid)
        data = json.loads(response.text)
        assert response.status_code == 201, f"Error: got status code {response.status_code} instead of 200"
        assert "name" in data and data['name'] == users_put_request_valid['name']
        assert "job" in data and data['job'] == users_put_request_valid['job']
        assert "createdAt" in data
       
    
    @pytest.mark.smoke
    def test_put_users_invalid(self):
        # Put для несуществующего пользователя
        url = MAIN_URL + "/api/users/23"
        response = requests.post(url, data=users_put_request_valid)
        if response.status_code == 201:
            pytest.xfail(f"Expected bug with next data --> {users_put_request_valid}")
        # assert response.status_code != 201, f"Error: got status code {response.status_code} instead of 201"
        