# Карина Шибалина, 7-я когорта — Финальный проект. Инженер по тестированию плюс

import requests as requests

import configuration
import data


def create_order():
    req = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=data.create_order_body)
    return req.json()["track"]


def get_order():
    params = {"t": create_order()}
    req = requests.get(configuration.URL_SERVICE+configuration.GET_ORDER, params=params)
    return req.status_code

print(get_order())


