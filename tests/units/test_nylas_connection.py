import logging
from datetime import datetime, timedelta

from officer.events.nylas_connection import NylasConnection


def test_nylas_meetings():
    from_date = datetime.utcnow()
    to_date = datetime.utcnow() + timedelta(days=1)
    connection = NylasConnection()
    meetings = connection.meetings(from_date, to_date)
    assert meetings is not None


def test_nylas_create_meeting():
    to_date = datetime.utcnow()
    start_date = to_date.date() + timedelta(days=1)
    connection = NylasConnection()
    meeting = connection.get_or_create_meeting('daily standup', start_date)
    assert meeting is not None
    logging.info(meeting)
    assert meeting.get('title') == 'daily standup'


def test_nylas_account():
    connection = NylasConnection()
    assert connection.account() is not None
    assert connection.messages() is not None
