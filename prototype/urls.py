"""
Definition of urls for prototype.
"""

from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

from customers import views

urlpatterns = [
    # Examples:
    # url(r'^$', prototype.views.home, name='home'),
    # url(r'^prototype/', include('prototype.prototype.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/customers', views.CustomerList.as_view())
]
