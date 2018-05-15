import pytest

from image_conveyor.core.http.app import get_app


@pytest.fixture
def app():
    return get_app()


@pytest.fixture
def good_task_params():
    return {
        'bucket': {
            'region': 'eu-central-1',
            'name': 'input-images-j4g23'
        },
        'files': ['test.jpg']
    }


def test_api_endpoint_success(client, good_task_params, monkeypatch):
    def fake_function(t):
        pass
    monkeypatch.setattr("image_conveyor.core.http.rest.add_task_to_queue", fake_function)
    response = client.post('/task/', json=good_task_params)
    assert response.status_code == 201, response


def test_api_endpoint_bad_request1(client, good_task_params):
    bad_task_params = good_task_params.copy()
    bad_task_params.pop('files')

    response = client.post('/task/', json=bad_task_params)
    assert response.status_code == 400
    assert 'errors' in response.json


def test_api_endpoint_bad_request2(client, good_task_params):
    bad_task_params = good_task_params.copy()
    bad_task_params.pop('bucket')

    response = client.post('/task/', json=bad_task_params)
    assert response.status_code == 400
    assert 'errors' in response.json