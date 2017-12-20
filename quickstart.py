from instapy import InstaPy
import os

insta_username = os.environ.get('INSTA_USER') 
insta_password = os.environ.get('INSTA_PW') 

# if you want to run this script on a server, 
# simply add nogui=True to the InstaPy() constructor
session = InstaPy(username=insta_username, password=insta_password)
session.login()

# set up all the settings
#session.set_upper_follower_count(limit=2500)
#session.set_do_comment(True, percentage=10)
#session.set_comments(['aMEIzing!', 'So much fun!!', 'Nicey!'])
#session.set_dont_include(['friend1', 'friend2', 'friend3'])
#session.set_dont_like(['pizza', 'girl'])

# do the actual liking
#session.like_by_tags(['natgeo', 'world'], amount=100)
session.follow_user_followers(['dublinveganhq'], amount=10, randomize=False)

# end the bot session
session.end()
