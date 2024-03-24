import sender_stand_request


# Проверка статуса заказа - код ответа равен 200:
def test_get_order_by_track():
    response = sender_stand_request.post_new_order()
    track = response.json()["track"]
    order_response = sender_stand_request.get_info_by_track_order(track)
    assert order_response.status_code == 200
