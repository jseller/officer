
Officer books the stand-up so you don't have to!

# Stories and Features
Developer wants to book daily standup. 
- check for daily standup
- book daily standup meeting if not found
- auto schedule the meeting 
-- schedule a status check before meeting time

# Functional Requirements

1. get events for dates
2. book a meeting
3. schedule a check for tomorrow

# Cross functional requirements #

## Usability ##
officer api returns standard json data
simple ui for setting the time and participaats

## Observability ##
- standard flask logging
- capture stdout in docker 

## Performance ##
TODO:
3. investigate caching policy
-- use redis for keys and account status
- cache api data since its doing a get and create
-- is there a way to check for schedule changes from a calendar?
-- data provider saves api data in cache
-- data provider updates cached data daily
-- meeting could get cancelled, so check just before meeting for cancellation

## Security
officer provide ssl connection
officer use tls (ssl connection with dependencies)

TODO
officer use native authentication
  - user accounts


# Deployment

docker compose up
- runs on port 5000

curl http://127.0.0.1:5000/events?from_date=2020-09-09&to_date=2020-09-11


# Development
-- add pre-commit hook for pipelines (bitbucker, github)

pipenv run pytest tests
pipenv run flake8

pipenv run flask run

# nylas-events

https://www.nylas.com/blog/the-nylas-neural-api-lean-code-machine-learning-for-communications-and-scheduling/
https://dashboard.nylas.com/applications/nylas_playground/settings/general
https://docs.nylas.com/reference#neural-categorize-message-put

tokens from nylas

## Gotchas ##

Can hang on messages without limit, any default limits to queries?

Get 500
https://dashboard.nylas.com/applications/ecwgleloykidsc9v2d6gajg5/logs/api

Page missing for oauth steps
https://support.nylas.com/hc/en-us/articles/222176307

Get developer API key - that wasnt super obvious
https://docs.nylas.com/docs/get-your-developer-api-keys

Typo on auth docs, had to look for the button
- inlined screen shots or video helps here
go to accounts and 'Add Account' not 'Auth account' in docs

Nice examples:
https://docs.nylas.com/docs/native-authentication
https://github.com/nylas/nylas-python/blob/main/examples/native-authentication-gmail/server.py

