# bunny_hn
Web app to connect voice bunny and hacker news web page.

== Configure ==

Register on voicebunny and get some credit. 
Then go to http://voicebunny.com/api-for-voice-overs/token and copy the API id 
and token to the bunny_hn/settings.py file variables:

BUNNY_API_ID
BUNNY_API_KEY

== Deploy instructions ==

Make sure you have both Python and virtualenv installed and then execute:

virtualenvenv ./
source ./bin/activate
python -m pip install -r requirements.txt
cd bunny_hn/
python manage.py migrate
python manage.py flush
python manage.py syncdb 
python manage.py runserver
