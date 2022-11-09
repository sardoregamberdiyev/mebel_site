from mebel_site.settings import DEFAULT_URL
import requests as rq

API_URL = DEFAULT_URL + "api/v1/"


def create_log(user_id):
    url = API_URL + "log/"
    data = {
        "user_id": user_id
    }
    resource = rq.post(url, data).json()
    return resource


def create_user(user_id):
    url = API_URL + "user/"
    data = {
        "user_id": user_id
    }
    resource = rq.post(url, data).json()
    return resource


def get_user(user_id):
    url = API_URL + "user/"
    response = rq.get(url)

    try:
        response = response.json()
    except:
        response = False

    return response


def get_log(user_id):
    url = API_URL + f"log/{user_id}/"
    response = rq.get(url)

    try:
        response = response.json()
    except:
        response = False

    return response

