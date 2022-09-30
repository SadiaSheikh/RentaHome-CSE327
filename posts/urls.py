from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



app_name = 'posts'
urlpatterns = [
    path('', views.post_list, name = 'list'),
    path('create_post/', views.post_create, name = "create"),
    path('post_detail/<id>/', views.post_detail, name = 'detail'),
    path('my_post', views.my_post, name = 'myPost'),
    path('search_bar/', views.search_bar, name = 'searchBar'),
    path('post_update/<id>/', views.post_update, name = 'update'),
    path('post_delete/<id>/', views.post_delete, name = 'remove'),
    path('post_filter', views.post_filters, name = 'filters'),
    path('contact.html', views.contact, name = "contact"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
