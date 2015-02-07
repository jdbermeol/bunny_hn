import requests
import simplejson
from requests.auth import HTTPBasicAuth
import logging
logger = logging.getLogger(__name__)


class BunnyAPI:

    def __init__(self, url, api_id, api_key):
        self.url = url
        self.api_id = api_id
        self.api_key = api_key

    def sendProject(self, title, script, test=1):
        req = requests.post(self.url + '/projects/addSpeedy',
                            data={'title': str(title) + 'bunny_hn',
                                  'script': str(script)},
                            auth=HTTPBasicAuth(self.api_id, self.api_key), verify=False)
        logger.info(req.text)
        print req.text
        data = simplejson.loads(req.text)

        if('project' in data):
            return data['project']
        elif('projects' in data):
            return data['projects'][0]

    def getProject(self, project_id):
        req = requests.get(self.url + '/projects/' + project_id,
                           auth=HTTPBasicAuth(self.api_id, self.api_key), verify=False)
        data = simplejson.loads(req.text)
        return data['projects'][0]
