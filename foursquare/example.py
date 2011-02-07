import os
from pprint import pprint

from api import Foursquare
from oauth import OAuth

if __name__ == '__main__':

    # say hello and ask for foursquare email/phone
    print('Foursquare API')
    print('--------------\n')
    username = raw_input('Email associated with your Foursquare account: ').strip()

    # build oauth obj, do oauth_dance if oath_token not available
    oauth_fname = '%s.token' % username
    if not os.path.exists(oauth_fname):
        raise Exception('need to do OAuth token getting blaaaah...')
    else:
        oauth_token = open(oauth_fname, 'r').readlines()[0]
        oauth_token = oauth_token.strip()
    auth = OAuth(oauth_token)

    # make our foursquare object
    fsq = Foursquare(auth=auth)

    # foursquare api requests
    phil_id = 5804431
    me = fsq.users()
    my_friends = fsq.users.friends(id=phil_id)
    pprint(me)
