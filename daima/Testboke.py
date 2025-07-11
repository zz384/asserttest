import  unittest

import requests
from parameterized import parameterized

from myboke.daima.duan import duan_yan
from myboke.daima.qianzhi import Test_qianzhi
from myboke.daima.read_jj import read_jjbo


class Test_login(unittest.TestCase):
    #登录成功
    @parameterized.expand(read_jjbo())
    def test_bokelogin(self,desc,req_data,status_code,success,code,message):
        json_data = req_data
        resp = Test_qianzhi.login(req_data)
        duan_yan(self,resp,code,success,message)
