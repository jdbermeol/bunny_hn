from django.conf.urls import patterns, url

urlpatterns = patterns('',
     url(r'^$', 'bunny_hn.views.home', name='home'),
     url(r'^hear_story/(?P<story_id>\d+)[/]?$', 'bunny_hn.views.getStory', name='hear_story'),
     url(r'^show_story[/]?$', 'bunny_hn.views.showStory', name='show_story'),
)
