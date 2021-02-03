import logging
from http import HTTPStatus


def test_can_get_events(testapp):
    res = testapp.get('/events')
    assert res.status_code == HTTPStatus.BAD_REQUEST
    res = testapp.get('/events?from_date=2020-09-09&to_date=2020-09-11')
    logging.info(str(res.json))
    assert res.status_code == HTTPStatus.OK
