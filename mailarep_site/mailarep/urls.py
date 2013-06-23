from django.conf.urls import patterns, include, url
from mailarep_app import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$',          views.index,     name='index'),
    # url(r'^mailarep/', include('mailarep.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

# Set the 404 View handler
handler404 = views.no_page_404_view
handler500 = views.server_error_500_view