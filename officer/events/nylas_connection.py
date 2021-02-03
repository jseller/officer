import logging
from datetime import datetime, timedelta

from nylas import APIClient

from officer.config import build_config

CONFIG = build_config()


class NylasConnection(object):

    def __init__(self):
        try:
            self.nylas = APIClient(
                CONFIG.API_CLIENT_ID,
                CONFIG.API_SECRET_KEY,
                CONFIG.API_ACCESS_TOKEN
            )
        except Exception as e:
            logging.exception(e)

    def account(self) -> dict:
        logging.info(self.nylas.account)
        return self.nylas.account

    def messages(self) -> str:
        message = self.nylas.messages.where(limit=10).all()
        return message

    def meetings(self, from_date, to_date) -> list:
        return self.nylas.events.all()

    def get_meeting(self, title, meeting_date) -> dict:
        return self.nylas.events.where(title=title).first()

    def build_meeting(self, calendar_id, title,
                      meeting_date: datetime) -> dict:
        meeting = self.nylas.events.create()
        meeting.title = title
        meeting.calendar_id = calendar_id
        end_time = meeting_date + timedelta(minutes=15)
        meeting.when = {'start_time': meeting_date.isoformat(),
                        'end_time': end_time.isoformat()}
        meeting.save()
        return meeting

    def get_or_create_meeting(self, title, start_date: datetime) -> dict:
        next_meeting = self.get_meeting(title, start_date)
        calendar_id = next_meeting.get('calendar_id')
        return self.build_meeting(calendar_id, title, start_date)
