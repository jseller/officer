
Officer books the stand-up so you don't have to!
- A standup meeting is a daily meeting between developers to discuss status. An Organizer books a time and send info to Developers

# Stories and Feature Requirements

OrganizerUser wants to book daily standup meeting. 
Given user account active on Officer and CalendarService
When organizer posts daily standup meeting info to StandupOrganizer
And includes a list of participants
Then meeting is scheduled on CalendarService
    And message returned with meeting details

StandupOrganizer schedules meeting
    While meeting is active
    When meeting has participants
        StandupOrganizer adds participants
            And adds participants to meeting details
        If participant is busy
            Then StandupOrganizer add message to meeting details
    When meeting has time
        When meeting window time is already scheduled in CalendarService
            Then notification is sent to DeveloperUser
        StandupOrganizer checks all participants calendars for conflicts
            if does not have user permission to see calendar
                set meeting status for participant
            check for overlapping times on calendar
    While meeting not found on CalendarService
        StandupOrganizer schedules meeting on CalenderService
        StandupOrganizer schedules reminder
    
StandupOrganizer cancels meeting
    When meeting is active
        StandupOrganzier removes time from CalendarService
        StandupOrganizer notifies participants with meeting status

DeveloperUser wants to set reminders of daily standup
While DeveloperUser has account 
When post preferences with reminder for meeting id or all meetings
Then get meeting prefrences

When StandupOrganizer executes reminder
    While user has preference for meeting reminders
        or meeting details has meeting reminder
        or default config for meeting reminder
    When ScheduledCheck checks meeting status
        StandupOrganizer notifies participants with meeting status
        
StandupMeeting
has time, participants
has more than one developer

OrganizerUser wants to confirm attendees
Given user account
When post user confirm on meeting and time to confirm after invite sent
Then update meeting status with confirmation

OrganizerUser wants auto confirm on calendar
Given user has preferences for confirming meeting
And officer has user credentials for CalendarService
Then StandupOrganizer confirms calendar meeting 
And sends reminder for meeting

StandupOrganizer gets manual confirmation
Given a meeting and meeting invite sent
When developeruser confirms or declines the meeting
Then the meeting status is updated for participant

Organizer user wants to book physical or virtual room for meeting
- Developers want to meet through video conferencing or room in the office
When rooom added to meeting details
    If organizer user has permission to book room
        Then Auth with service on behalf of user
- add attendees to meeting room
- add room/video conference details to meeting status

Organizer wants agenda for standup
- participants use agenda service to track tasks, notes and events



# Functional Requirements
User wants to keep credentials in officer for service so they don't have to manually auth
Officer authticates with services on behalf of user
Given user authenticated on officer
And user account on service
When user authorizes officer to authenticate with service
Then user is able to get account details from officer
And from authenticated service

Ubiiquitous:
OfficerAuth has User Login
- When user adds username and password,
    While officer has user account, 
        And username and password match
        Then Auth starts session
    If user does not have account
        Auth generates message for User Signup

OfficerAuth has User Signup
- When user adds username and password,
    If user confirms email,
        Auth creates user account
    if username already exits
        Auth generates user exits message 

OfficerAuth connects to ServiceAuth
- When user connects to ServiceAuth
    then Auth uses username from service
        and creates a user session
        While officer has user service credentials, officer connects to service

Officer Service Oauth Authenticatiion
    While Auth has user account,
        While Auth has service credentials
            Auth creates session on service
        If Auth does not have service credential
            Auth generates error message
    When ServiceAuth has no service session
        While auth provider has refresh token
        And submits token to service
            When service returns access token
                ServiceAuth starts service session
            If service returns error
                Then ServiceAuth generates message on lack of service
    If ServiceAuth does not have refresh token
        Then ServiceAuth generates message requiring oauth connection


Officer has Components:
OfficerAuth
ServiceAuth

Feature
- officer uses native authentication with services and user accounts

| officer 
- user
| calendarservice |
- google, ms
| meeting service |
- zoom

# Cross functional requirements 


## Usability
officer api returns standard json data
simple ui for setting the time and participaats

## Observability
- standard flask logging
- capture stdout in docker 

## Performance
TODO:
3. investigate caching policy
-- use redis for keys and account status
- cache api data since its doing a get and create
-- is there a way to check for schedule changes from a calendar?
-- data provider saves api data in cache
-- data provider updates cached data daily
-- meeting could get cancelled, so check just before meeting for cancellation

## Security
officer provide ssl connection to services ()
officer use tls (ssl connection with dependencies)


# Development
-- add pre-commit hook for pipelines (bitbucker, github)

pipenv run pytest tests
pipenv run flake8
pipenv run flask run


Python —version
Use pyenv to to upgrade to python3
Get brew from brew.sh
brew install pyenv
Add pyenv to .zrcsh for commands => https://ducfilan.wordpress.com/2017/11/13/manage-versions-of-python-with-pyenv-and-zsh-in-macos/
pyenv install 3.6.8
pyenv versions
pyenv global 3.6.8



# Deployment

docker compose up
- runs on port 5000

curl http://127.0.0.1:5000/events?from_date=2020-09-09&to_date=2020-09-11



## Trial account Gotchas

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


# Methodology

# Story -> Feature -> Requirements
Create Story (who, what, why)
Write BDD acceptance criteria from story goal
- Add to features
Write functional spec in EARS syntax
- Add to architecture/engineering (context:requirements) (container:component)
- Context and resposibilty http://www.wirfs-brock.com/PDFs/A_Brief-Tour-of-RDD.pdf
Add issue for implementation
- add Link to feature and functional spec
Link issue to feature
Use epic for release version
- add relevant issues to epic

Feature
- Story
- BDD
Functional requirements 
- EARS
- https://aaltodoc.aalto.fi/bitstream/handle/123456789/12861/D5_uusitalo_eero_2012.pdf

TDD Spec DD
- spec has structure and behaviour

base without dependencies
base with mocked dependencies injected
base wth live dependencies

mutate parameters (inputs) https://software.rajivprab.com/2021/02/04/mutation-driven-testing-when-tdd-just-isnt-good-enough/?utm_source=thevaluabledev&utm_medium=email
mutate configuration
