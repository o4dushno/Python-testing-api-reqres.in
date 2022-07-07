from payloads import login_schema, login_request_valid, register_request_valid, register_schema, list_users_schema, \
    users_create_request_valid, users_create_schema
from jsonschema import validate
from config import MAIN_URL
import requests


login_url = MAIN_URL + "/api/login"
register_url = MAIN_URL + "/api/register"
list_users_url = MAIN_URL + "/api/users?page=2"
users_create_url = MAIN_URL + "/api/users"


def test_login_schema():
    response = requests.post(login_url, data=login_request_valid)
    validate(instance=response.json(), schema=login_schema)

def test_register_schema():
    response = requests.post(register_url, data=register_request_valid)
    validate(instance=response.json(), schema=register_schema)

def test_users_schema():
    response = requests.get(list_users_url)
    validate(instance=response.json(), schema=list_users_schema)
    
def test_users_create_schema():
    response = requests.post(users_create_url, data=users_create_request_valid)
    validate(instance=response.json(), schema=users_create_schema)