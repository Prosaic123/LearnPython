import requests

class NetworkUtils:
    @staticmethod
    def get(url):
        """发送 GET 请求"""
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        return response.text

    @staticmethod
    def post(url, data):
        """发送 POST 请求"""
        response = requests.post(url, json=data)
        response.raise_for_status()  # 检查请求是否成功
        return response.json()
