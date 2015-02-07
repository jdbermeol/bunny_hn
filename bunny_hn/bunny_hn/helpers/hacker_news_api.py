from bunny_hn.models import StoryVo
import requests
import simplejson
import logging
import time
logger = logging.getLogger(__name__)


class HackerNewsAPI:

    def __init__(self, url, max_attempts=3):
        self.max_attempts = max_attempts
        self.url = url

    def getTopStories(self, number=10):
        error = True
        attempts_count = 0
        while(error and attempts_count < self.max_attempts):

            req = requests.post(self.url + '/v0/topstories.json', verify=False)
            req.headers['User-Agent'] = 'bunny_hn/0.1'
            data = simplejson.loads(req.text)
            if('error' in data):
                logger.info(data['error'])
                time.sleep(5)
            else:
                error = False
            attempts_count += 1

        if(error):
            raise Exception("Could not get trending")
        return data[:number]

    def getStory(self, story_id):
        error = True
        attempts_count = 0
        while(error and attempts_count < self.max_attempts):
            req = requests.post(self.url + '/v0/item/' + str(story_id) + '.json', verify=False)
            req.headers['User-Agent'] = 'bunny_hn/0.1'
            data = simplejson.loads(req.text)
            if('error' in data):
                logger.info(str(data['error']))
                time.sleep(5)
            else:
                error = False
            attempts_count += 1
        if(error):
            raise Exception("No story with id " + str(story_id))

        return StoryVo(story_id, data['by'], data['score'], data['title'], data['url'])
