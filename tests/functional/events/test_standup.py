
from datetime import datetime
from http import HTTPStatus


import pytest


payload = {'date': datetime.utcnow().isoformat()}


def test_can_create_standup(testapp):
    res = testapp.post('/standup',
                       json=payload)
    assert res.status_code == HTTPStatus.OK
    assert res.json.get('title') == 'standup'
    meeting_start = res.json.get('when').get('start_time')
    start_date = datetime.fromtimestamp(meeting_start)
    assert start_date.date() == datetime.utcnow().date()


@pytest.mark.parametrize('field, value, error_message', [
    pytest.param('date', '', 'Field may not be null.',
                 id='missing date')
])
def test_create_standup_validations(testapp, field, value, error_message):
    payload[field] = value
    res = testapp.post('/standup',
                       json=payload)
    assert res.status_code == HTTPStatus.BAD_REQUEST
    assert res.json['description'] == 'Input failed validation.'
