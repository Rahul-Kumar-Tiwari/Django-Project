from django.conf.urls import url

#VIEWSET
from django.conf.urls import include
from rest_framework.routers import DefaultRouter


from . import views


#VIEWSET
router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet, base_name='hello-viewset')
router.register('profile',views.UserProfileViewSet)




urlpatterns = [
	url(r'^hello-view/', views.HelloApiView.as_view()),
# fed to router because its empty
	url(r'',include(router.urls)),
]