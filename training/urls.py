from django.urls import path
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('delete/<int:Aadhar>', views.delete, name='delete'),
    path('update/<int:Aadhar>', views.update, name='update'),
    path('do-update/<int:Aadhar>', views.doupdate, name='doupdate'),
    path('TrL/', views.TravellerList.as_view(), name='TrL'),
    path('TrL/<int:pk>', views.Traveller_detail.as_view(), name='TrL'),
    path('users/', views.UserList.as_view(),name='users'),
    path('users/<int:pk>/', views.UserDetail.as_view(),name='users'),
    path('upload/', views.upload_file,name='upload'),
    
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
 urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)