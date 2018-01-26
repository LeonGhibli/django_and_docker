from django.conf.urls import url
from . import views
from . import api_v1

app_name = 'users' 



urlpatterns = [
    url(
        regex=r'^$',
        view=views.UserListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^~redirect/$',
        view=views.UserRedirectView.as_view(),
        name='redirect'
    ),
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^~update/$',
        view=views.UserUpdateView.as_view(),
        name='update'
    ),
    url(r'^api/v1/hello_1/(?P<hello_message>.+)$', api_v1.Hello_Tracker_1.as_view(), name='hello_tracker_1'),
    url(r'^api/v1/hello_2/$', api_v1.Hello_Tracker_2.as_view(), name='hello_tracker_2'),   
]
