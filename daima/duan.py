def duan_yan(self,resp,code,success,message):
    self.assertEqual(code, resp.json().get("code"))
    self.assertEqual(success, resp.json().get("success"))
    self.assertIn(message, resp.json().get("message"))