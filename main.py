import sys
import json
import requests

if __name__ == "__main__":
    # Receive a GitHub username from the command line
    username = sys.argv[1]
    #username = 'jjame369'

    response = requests.get("https://api.github.com/users/{}/events".format(username))
    # Retrieve a list of "events" associated with that user. User events include things like pushing to a repository
    # or opening up an issue on a repository.
    events = json.loads(response.content)

    # Print out the time stamp associated with the first event in that list
    print(events[0]['created_at'])



