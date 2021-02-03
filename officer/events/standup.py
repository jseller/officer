import logging
from datetime import datetime, timedelta

from officer.config import build_config
from officer.events.nylas_connection import NylasConnection
from officer.extensions import scheduler

CONFIG = build_config()


class StandupOrganizer(object):

    @staticmethod
    def check_meeting(event_id):
        logging.info('scheduler validate reminder '+str(event_id))
        with scheduler.app.app_context():
            connection = NylasConnection()
            meeting = connection.get_meeting(event_id)
            if meeting is None or meeting.status != 'confirmed':
                meeting = connection.get_or_create_meeting()

    @staticmethod
    def schedule(meeting):
        if CONFIG.SCHEDULER is False:
            logging.info('Scheduing is off ')
            return
        job_id = meeting.get('id')
        # check 30mins before
        check = datetime.fromtimestamp(meeting.get('when').get('start_time'))
        check = check - timedelta(minutes=30)
        scheduler.add_job(id=job_id,
                          func=StandupOrganizer.check_meeting,
                          trigger='interval', days=1,
                          start_date=check.isoformat(),
                          args=[meeting.id])
