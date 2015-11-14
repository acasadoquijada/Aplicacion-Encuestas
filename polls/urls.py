from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
	url(r'^createpoll/$', views.createPoll, name='createPoll'),
	url(r'^createpoll/newpoll/$', views.newPoll, name='newPoll'),
	url(r'^deletepoll/$', views.deletePoll, name='deletePoll'),
	url(r'^deletepoll/deleted$', views.deleteOnePoll, name='deleteOnePoll'),
    url(r'^polls/$', views.polls),

]
