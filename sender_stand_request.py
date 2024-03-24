import configuration
import requests
import data


# Создание заказа клиентом:
def post_new_order():
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER,
        json=data.order_body,
        headers=data.headers_content_type
    )


# Получение данных о заказе по треку:
def get_info_by_track_order(track):
    return requests.get(
        configuration.URL_SERVICE + configuration.TRACK_ORDER,
        params={
            "t": track
        }
    )
