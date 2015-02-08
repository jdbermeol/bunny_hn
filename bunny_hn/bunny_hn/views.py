from bunny_hn.models import Story
from bunny_hn.helpers.hacker_news_api import HackerNewsAPI
from bunny_hn.helpers.bunny_api import BunnyAPI
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

hacker_news_api = HackerNewsAPI(settings.HACKERNEWS_URL)
bunny_api = BunnyAPI(settings.BUNNY_URL, settings.BUNNY_API_ID, settings.BUNNY_API_KEY)


def home(request):
    stories_id = hacker_news_api.getTopStories(5)
    stories = []
    for story_id in stories_id:
        stories.append(hacker_news_api.getStory(story_id))
    context = {'stories': stories}
    return render(request, 'home.html', context)


def getStoryAudio(request, story_id):
    story = None
    try:
        story = Story.objects.get(story_id__exact=story_id)
        project = bunny_api.getProject(story.bunny_project_id)
        story.status = project['reads'][0]['status']
        story.save()
    except ObjectDoesNotExist:
        data = request.POST
        project = bunny_api.sendProject(story_id, data['title'])
        bunny_project_id = project['id']
        audio_url = project['reads'][0]['urls']['part001']['original']
        status = project['reads'][0]['status']
        story = Story(story_id, data['by'], data['score'], data['title'], data['url'],
                      bunny_project_id, audio_url, status)
        story.save()


def getStory(request, story_id):
    getStoryAudio(request, story_id)
    return HttpResponseRedirect(reverse('show_story', args=(story_id,)))


def showStory(request, story_id):
    story = get_object_or_404(Story, pk=story_id)
    return render(request, 'show_story.html', {'story': story})
