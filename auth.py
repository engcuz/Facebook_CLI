
# authentication and authorization
from hashlib import sha256

from flask import request, g, session, redirect, url_for
from sqlalchemy.exc import SQLAlchemyError
from http import HTTPStatus
import base64
from passlib.hash import pbkdf2_sha256
from datetime import datetime, timedelta

import time
import requests
from requests_oauthlib import OAuth2Session #  class

# acebook app credentials
client_id = '2815685951939270'  
client_secret = '9cf13d000e28c640e9595f676845a709'  

#  ngrok URL, I added this url to  "OAuth Redirect URIs" in fb devleper
redirect_uri = "https://85adb18e8086.ngrok.app/callback"  # Replace with your ngrok URL

# call back url wher fb will redirect user after authtiticate 



# Facebook OAuth2 URLs
authorization_base_url = 'https://www.facebook.com/v12.0/dialog/oauth'

# to exchange  authorization code for access token. 
#  access token grant permission for app to make authorized requests on behalf of the user
token_url = 'https://graph.facebook.com/v12.0/oauth/access_token'



def get_facebook_auth_url():
    
    # generates  fb authorization URL.
    # return tuple containing  authorization url and  state token.
    # CSRF protection used 
    facebook = OAuth2Session(client_id, redirect_uri=redirect_uri) # create OAth session
    #
    auth_url, state = facebook.authorization_url(authorization_base_url)
    return auth_url, state

def get_token(code):

    # initializes OAuth 2.0 session with the fb client ID and redirect URI
    facebook = OAuth2Session(client_id, redirect_uri=redirect_uri)
    # request token from fb, send 
    token_data = facebook.fetch_token(token_url, client_secret=client_secret, code=code)
    
    # set the token to expire in 30 minutes 
    token_data['expires_at'] = (datetime.now() + timedelta(minutes=30)).timestamp()
    
    return token_data
