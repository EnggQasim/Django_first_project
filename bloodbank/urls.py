from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from bloodbank import views
app_name="bloodbank"
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<donor_id>[0-9]+)/', views.details, name='details'),
    url(r'^export/', views.DonorList.as_view()),
    url(r'^Register/', views.signup, name='signup'),
    url(r'^Register/add/', views.add_donor, name='add_donor'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^login/', views.login, name='login'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
