""" Test Login """

login_request_valid = {
    "email": "eve.holt@reqres.in", 
    "password": "pistol"
}

login_response_valid = {
    'token': "QpwL5tke4Pnpja7X4"
}

login_request_invalid = [
    # Авторизация с неправильным логином
    {
        "email": "bad_email@mail.com",
        "password": "cityslicka"
    },
    # Авторизация с пустым логином
    {
        "email": "",
        "password": "cityslicka"
    },
    # Авторизация с пустым логином
    {
        "email": " ",
        "password": "cityslicka"
    },
    # Авторизация с неправильным паролем
    {
        "email": "eve.holt@reqres.in",
        "password": "qwerty123123123"
    },
    # Авторизация с пустым паролем
    {
        "email": "eve.holt@reqres.in",
        "password": ""
    },
    # Авторизация с пустым паролем
    {
        "email": "eve.holt@reqres.in",
        "password": " "
    },
    # Авторизация без email
    {
        "password": "cityslicka"
    },
    # Авторизация без пароля
    {
        "email": "bad_email@mail.com"
    },
]

login_schema = {"type": "object",
    "required": [
        "token"
    ],
    "properties": {
        "token": {
            "type": "string",
            "title": "The token Schema"
        }
    }
}

""" Test Registratoin """

register_request_valid = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

register_response_valid = {
    "id": 4,
    "token": "QpwL5tke4Pnpja7X4"
}

register_request_invalid = [
    # Использоание неправильного email
    {
        "email": "wrong_email",
        "password": "pistol"
    },
    # Регистрация с пустым email
    {
        "email": "",
        "password": "pistol"
    },
    # Пробел в email
    {
        "email": " ",
        "password": "pistol"
    },
    # Неправильный (для данного api) пароль
    {
        "email": "eve.holt@reqres.in",
        "password": "wrong_password"
    },
    # Пустой пароль
    {
        "email": "eve.holt@reqres.in",
        "password": ""
    },
    # Пробел вместо пароля
    {
        "email": "eve.holt@reqres.in",
        "password": " "
    },
    # Неправильный логин и пароль
    {
        "email": "wrong@mail.ru",
        "password": "wron_password"
    },
    # Отсутствие параметра email
    {
        "password": "pistol"
    },
    # Отсуствие параметра password
    {
        "email": "eve.holt@reqres.in"
    },
]

register_schema = {
    "type": "object",
    "default": {},
    "title": "Root Schema",
    "required": [
        "id",
        "token",
    ],
    "properties": {
        "id": {
            "type": "integer",
            "title": "The id Schema",
            "examples": [
                2
            ],
        },
        "token": {
            "type": "string",
            "title": "The token Schema",
            "examples": [
                "QpwL5tke4Pnpja7X4"
            ],
        },
    },
    
    "examples": [{
        "id": 4,
        "token": "QpwL5tke4Pnpja7X4"
    }]
}


""" Test users """

users_create_request_valid = {
    "name": "morpheus",
    "job": "leader"
}


users_create_response_valid = {
    "name": "morpheus",
    "job": "leader",
    "id": "857",
    "createdAt": ""
}


users_create_response_invalid = [
    # Пользователь без имени
    {
        "job": "leader"
    },
    # Пользователь без работы
    {
        "name": "morpheus",
    },
    # Пробел вместо имени
    {
        "name": " ",
        "job": "leader"
    },
    # Пробел вместо работы
    {
        "name": "UserName",
        "job": " "
    },
]

users_put_request_valid = {
    "name": "morpheus",
    "job": "zion resident"
}


list_users_schema = {
    "type": "object",
    "required": [
        "page",
        "per_page",
        "total",
        "total_pages",
    ],
    "properties": {
        "page": {
            "type": "integer"
        },
        "per_page": {
            "type": "integer"
        },
        "total": {
            "type": "integer"
        },
        "total_pages": {
            "type": "integer"
        },
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "required": [
                    "id",
                    "email",
                    "first_name",
                    "last_name",
                    "avatar",
                ],
                "properties": {
                    "id": {
                        "type": "integer",
                    },
                    "email": {
                        "type": "string",
                    },
                    "first_name": {
                        "type": "string",
                    },
                    "last_name": {
                        "type": "string",
                    },
                    "avatar": {
                        "type": "string",
                    },
                }
            }
        },
        "support": {
            "type": "object",
            "required": [
                "url",
                "text"
            ],
            "properties": {
                "url": {
                    "type": "string",
                },
                "text": {
                    "type": "string",
                }
            }
        }
    }
}

users_create_schema = {
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "job": {
      "type": "string"
    },
    "id": {
      "type": "string"
    },
    "createdAt": {
      "type": "string"
    }
  },
  "required": [
    "name",
    "job",
    "id",
    "createdAt"
  ]
}

