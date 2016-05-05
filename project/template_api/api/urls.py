from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^api/$', views.api_root),
    url(
        r'^api/snippets/$',
        views.TemplateSnippetList.as_view(),
        name='snippet-list'
    ),
    url(
        r'^api/snippets/(?P<pk>[0-9]+)/$',
        views.TemplateSnippetDetail.as_view(),
        name='snippet-detail'
    ),
    url(r'^api/users/$', views.UserList.as_view(), name='user-list'),
    url(
        r'^api/users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user-detail'
    ),
    url(r'^api/register/$', views.UserCreate.as_view(), name='register')
]
