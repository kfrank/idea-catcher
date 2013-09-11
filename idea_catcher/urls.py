from django.conf.urls import patterns, include, url
from app import views
from app.views import idea_list, new_idea

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^list/$', idea_list),
    url(r'^new/$', new_idea),
    # url(r'^$', 'idea_catcher.views.home', name='home'),
    # url(r'^idea_catcher/', include('idea_catcher.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
