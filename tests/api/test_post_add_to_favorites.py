import json

from diplom_qa_guru.utils.request_helper import api_post


def test_post_add_to_favorites():
    url = "/favorites/add"
    data = json.dumps({
        "productId":
            1299225
    })
    url_remove = "/favorites/remove"

    response = api_post(url, data=data)
    assert response.status_code == 200
    assert response.json()['timestamp']
    result = api_post(url=url_remove, data=data)
    assert result.json()['timestamp']
