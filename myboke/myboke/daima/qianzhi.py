import requests


class Test_qianzhi(object):
    @classmethod
    def login(cls,json_data):
        resp = requests.post(url="http://127.0.0.1:5000/api/login",json=json_data)
        return resp