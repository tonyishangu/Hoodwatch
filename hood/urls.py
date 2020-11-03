from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
from django.urls import path, include


urlpatterns = [
    url('^$', views.index, name='index'),
    url('^signup/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('all-hoods/', views.hoods, name='hood'),
    path('new-hood/', views.create_hood, name='new-hood'),
    path('profile/<username>', views.profile, name='profile'),
    path('profile/<username>/edit/', views.edit_profile, name='edit-profile'),
    path('join_hood/<id>', views.join_hood, name='join-hood'),
    path('leave_hood/<id>', views.leave_hood, name='leave-hood'),
    path('single_hood/<hood_id>', views.single_hood, name='single-hood'),
    path('<hood_id>/new-post', views.create_post, name='post'),
    path('<hood_id>/members', views.hood_members, name='members'),
    path('search/', views.search_business, name='search'),
    url('^api/profiles/$', views.ProfileList.as_view(), name='profile_list'),
    url('^api/neighbourhood/$', views.NeighbourhoodList.as_view(),
        name='neighbourhood_list'),
    url('^api/business/$', views.Business_centresList.as_view(),
        name='business_center_list'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
