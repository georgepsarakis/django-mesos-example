from django.conf.urls import url, include
from .views import home

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^$', home),
    url(r'^', include('api.urls')),
    url(r'^api-auth/',
        include(
            'rest_framework.urls',
            namespace='rest_framework'
        )
    )
]
