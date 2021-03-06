from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^accounts/$', 'accounts.views.index'),
    url(r'^accounts/register', 'accounts.views.register'),
    url(r'^accounts/login', 'accounts.views.userlogin'),
    url(r'^accounts/logout','accounts.views.userlogout'),
    url(r'^accounts/uploadfile','accounts.views.save_file'),
    url(r'^$', 'frontend.views.index'),
    #url(r'^accounts/confirm', 'accounts.views.confirm'),
    # Examples:
    #url(r'^$', 'briefcase.views.home', name='home'),
    # url(r'^briefcase/', include('briefcase.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
