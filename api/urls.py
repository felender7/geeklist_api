from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from api import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api/api$', views.geek_list),
    #url(r'^api/api/(?P<pk>[0-9]+)$', views.geek_list_detail),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
