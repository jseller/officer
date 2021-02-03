from flask import Blueprint, jsonify, render_template

from officer.events.nylas_connection import NylasConnection
from officer.events.standup import StandupOrganizer

from webargs import fields
from webargs.flaskparser import use_args

blueprints = Blueprint('blueprints', __name__)


@blueprints.route('/')
def builder():
    return render_template('index.html')


@blueprints.route('/events', methods=['GET'])
@use_args({'from_date': fields.Str(required=True),
           'to_date': fields.Str(required=True)}, location='query')
def get_events(args):
    connection = NylasConnection()
    meetings = connection.meetings(args.get('from_date'),
                                   args.get('to_date'))
    # add marshmallow schema for serialization
    result = [{'title': meeting.title,
               'when': meeting.when} for meeting in meetings]
    return jsonify(result)


@blueprints.route('/standup', methods=['POST'])
@use_args({'date': fields.DateTime(required=True)}, location='json')
def standup(args):
    connection = NylasConnection()
    meeting = connection.get_or_create_meeting('standup', args.get('date'))
    StandupOrganizer.schedule(meeting)
    result = {'title': meeting.title, 'when': meeting.when}
    return jsonify(result)
