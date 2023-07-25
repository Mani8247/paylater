from unittest import TestCase, main
import json
import requests

class TestCases(TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    
    def test_new_user(self):

        url = "http://127.0.0.1:8000/newUser"

        payload = json.dumps({
        "name": "Indu",
        "email": "indu@gmail.com",
        "balance": 1100
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        
        self.assertEqual(response["status"], "success")

    def test_new_merchant(self):
        url = "http://127.0.0.1:8000/newMerchant"

        payload = json.dumps({
        "name": "pizzahut",
        "email": "pizzahut@gmail.com",
        "fee": 6
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        self.assertEqual(response["status"], "success")

    def test_new_transaction(self):
        url = "http://127.0.0.1:8000/transact"

        payload = json.dumps({
        "u_id": 5,
        "m_id": 5,
        "amount": 300
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        self.assertEqual(response["status"], "success")

    def test_merchant(self):
        url = "http://127.0.0.1:8000/getMerchant/6"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        self.assertEqual(response["status"], "success")

    def test_update_fees(self):
        url = "http://127.0.0.1:8000/updateFee?mid=4&fee=2"

        payload = {}
        headers = {}

        response = requests.request("POST", url, headers=headers, data=payload)
        self.assertEqual(response["status"], "success")

    def test_repay(self):
        url = "http://127.0.0.1:8000/repay?name=Indu&amount=200"

        payload = {}
        headers = {}

        response = requests.request("POST", url, headers=headers, data=payload)
        self.assertEqual(response["status"], "success")

    def test_fee(self):
        url = "http://127.0.0.1:8000/fee/neos"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        self.assertEqual(response["status"], "success")

    def test_dues(self):
        url = "http://127.0.0.1:8000/dues/Mani"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        self.assertEqual(response["status"], "success")

    def test_useratlimit(self):
        pass

    def test_totaldues(self):
        url = "http://127.0.0.1:8000/totalDues"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        self.assertEqual(response["status"], "success")
    
    def test_some_test_Case(self):
        pass
        """
        1. When user limit exceedds should "Return insuffcient funds!" as messasge
        """
        
if __name__ == '__main__':
    main()
    