import logging

from officer.config import build_config

import requests

CONFIG = build_config()


class GmailConnection(object):

    def build_native_auth(self, user_name, email):
        gmail_authentication = {
            'client_id': CONFIG.API_CLIENT_ID,
            'name':          user_name,
            'email_address': email,
            'provider':      'gmail',
            'settings':      {
                'google_client_id':     CONFIG.GOOGLE_CLIENT_ID,
                'google_client_secret': CONFIG.GOOGLE_CLIENT_SECRET
            },
            'scopes': 'email,calendar,contacts'
        }
        nylas_authorization = requests.post(
                'https://api.nylas.com/connect/authorize',
                json=gmail_authentication
        )
        nylas_code = nylas_authorization.json()['code']
        logging.info(nylas_code)
        return nylas_code
