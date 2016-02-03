from rest_framework.routers import DefaultRouter
from django.conf.urls import patterns, url, include
from api.views import (
	PingView, UserViewSet, OrganizationViewSet, TeamViewSet
)


user_list = UserViewSet.as_view({
    'get': 'list'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

organization_list = OrganizationViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

organization_detail = OrganizationViewSet.as_view({
	'get': 'retrieve',
	'put': 'update',
	'patch': 'partial_update',
	'delete': 'destroy'
})

team_list = TeamViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

team_detail = TeamViewSet.as_view({
	'get': 'retrieve',
	'put': 'update',
	'patch': 'partial_update',
	'delete': 'destroy'
})

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'organizations', OrganizationViewSet)
router.register(r'teams', TeamViewSet)

urlpatterns = patterns('',
	url(r'^', include(router.urls)),
	url(r'ping/$', PingView.as_view(), name='ping'),
	url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
)