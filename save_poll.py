from sys import argv

from Lib.Workspace import parse_json
from Lib.Mongo import insert

polls = argv[1:]

for poll in polls:
    poll_contents, poll_name = parse_json(poll)
    insert(poll_contents, 'Polls')
