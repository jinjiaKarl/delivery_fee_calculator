from app.main import app

def test_delivery_success():
    cart = {"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2021-10-12T13:00:00Z"}
    response = app.test_client().post('/',json=cart)

    assert response.status_code == 200
    assert response.json == {"delivery_fee": 710}

def test_delivery_free():
    cart = {"cart_value": 10000, "delivery_distance": 2235, "number_of_items": 4, "time": "2021-10-12T13:00:00Z"}
    response = app.test_client().post('/',json=cart)

    assert response.status_code == 200
    assert response.json == {"delivery_fee": 0}

def test_delivery_invalid():
    cart = {"cart_value": "aa", "delivery_distance": 2235, "number_of_items": 4, "time": "2021-10-12T13:00:00Z"}
    response = app.test_client().post('/',json=cart)
    assert response.status_code == 400
    assert response.json == {"error": "Invalid input"}

    cart = {"delivery_distance": 2235, "number_of_items": 4, "time": "2021-10-12T13:00:00Z"}
    response = app.test_client().post('/',json=cart)
    assert response.status_code == 400
    assert response.json == {"error": "Invalid input"}

