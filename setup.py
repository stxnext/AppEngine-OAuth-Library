
try:
    from setuptools import setup
except ImportError:
    from distutils import setup

long_description="""\
A simple OAuth implementation for authenticating users with third party
websites.

A typical use case inside an AppEngine controller would be:

1) Create the OAuth client. In this case we'll use the Twitter client,
  but you could write other clients to connect to different services.

  import oauth

  consumer_key = "LKlkj83kaio2fjiudjd9...etc"
  consumer_secret = "58kdujslkfojkjsjsdk...etc"
  callback_url = "http://www.myurl.com/callback/twitter"

  client = oauth.TwitterClient(consumer_key, consumer_secret, callback_url)

2) Send the user to Twitter in order to login:

  self.redirect(client.get_authorization_url())

3) Once the user has arrived back at your callback URL, you'll want to
  get the authenticated user information.

  auth_token = self.request.get("oauth_token")
  auth_verifier = self.request.get("oauth_verifier")
  user_info = client.get_user_info(auth_token, auth_verifier=auth_verifier)

  The "user_info" variable should then contain a dictionary of various
  user information (id, picture url, etc). What you do with that data is up
  to you.

  That's it!

4) If you need to, you can also call other other API URLs using
  client.make_request() as long as you supply a valid API URL and an access
  token and secret. Note, you may need to set method=urlfetch.POST.

@author: Mike Knapp
@copyright: Unrestricted. Feel free to use modify however you see fit. Please
note however this software is unsupported. Please don't email me about it. :)
"""

setup(
    name="oauth",
    version="0.1.4",
    description='',
    long_description=long_description,
    author="Mike Knapp",
    author_email="",
    url="",
    py_modules=["iso8601"],
)
