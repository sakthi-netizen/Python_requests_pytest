import requests

class APICLIENT:
    BASE_URL = "https://jsonplaceholder.typicode.com"
    def __init__(self):
        self.header = {
            "Content-Type": "application/json",
        }
    def get(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url,headers=self.header)
        return response

    def post(self, endpoint, data):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.post(url,headers=self.header,json=data)
        return response

    def put(self, endpoint, data):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.put(url,headers=self.header,json=data)
        return response
    
    def delete(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.delete(url,headers=self.header)
        return response