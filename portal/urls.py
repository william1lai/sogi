from django.conf.urls import url, include
from portal.views import *

urlpatterns = [

    url(r'^$', portal_main_page),
    url(r'^mysongs/$', my_songs_page),
    url(r'^mysongs/addsong/$', add_song_page),
    url(r'^mysongs/edit/(?P<sid>[0-9]*)$', edit_song_page),
    url(r'^mysongs/remove/(?P<sid>[0-9]*)$', remove_song),
    url(r'^history/gift/(?P<uid>[0-9]*)$', gift_history),
    url(r'^history/rate/(?P<uid>[0-9]*)$', rate_history),
    url(r'^group/create/$', create_group_page),
    url(r'^group/join/$', join_group_page),
    url(r'^group/(?P<gid>[0-9]*)$', group_page),
    url(r'^group/(?P<gid>[0-9]*)/leave/$', leave_group),
    url(r'^group/(?P<gid>[0-9]*)/start_turn/$', start_turn),
    url(r'^group/(?P<gid>[0-9]*)/end_turn/$', end_turn),
    url(r'^group/(?P<gid>[0-9]*)/gift/$', gift_page),
    url(r'^group/(?P<gid>[0-9]*)/gift/(?P<sid>[0-9]*)$', gift_song),
    url(r'^group/(?P<gid>[0-9]*)/rate/(?P<sid>[0-9]*)$', rate_song),
    url(r'^group/(?P<gid>[0-9]*)/alreadyheard/(?P<sid>[0-9]*)$', 
        already_heard),
    url(r'^group/(?P<gid>[0-9]*)/autogift/', auto_gift),
    
]
