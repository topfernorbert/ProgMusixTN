import requests

def test_postman_1():
    url = "http://localhost:8080/api/categories"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    assert response.text == '[{"id":1,"name":"WOODWIND"},{"id":2,"name":"BRASS INSTRUMENTS"},{"id":3,"name":"PERCUSSION INSTRUMENTS"},{"id":4,"name":"KEYBOARD INSTRUMENTS"},{"id":5,"name":"GUITAR FAMILY"},{"id":6,"name":"BOWED STRINGS"},{"id":7,"name":"MISC"},{"id":14,"name":"TRADITIONAL"}]'
