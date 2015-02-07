from django.db import models


class Story(models.Model):
    story_id = models.IntegerField(primary_key=True)
    by = models.CharField(max_length=30)
    score = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    bunny_project_id = models.CharField(max_length=30)
    audio_url = models.CharField(max_length=30)
    status = models.CharField(max_length=30)


class StoryVo:

    def __init__(self, story_id, by, score, title, url):
        self.story_id = story_id
        self.by = by
        self.score = score
        self.title = title
        self.url = url
