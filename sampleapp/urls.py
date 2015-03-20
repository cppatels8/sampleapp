from django.conf.urls import patterns, include, url
from django.contrib import admin

from tastypie.api import Api
from searchapp.resources import MPattendenceResource

v1_api = Api(api_name='v1')

v1_api.register(MPattendenceResource())

urlpatterns = patterns('',
    
    (r'^api/', include(v1_api.urls)),
    # Examples:
    # url(r'^$', 'sampleapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('^$', 'searchapp.views.home', name='home'),
    url('^load-data$', 'searchapp.views.load_csv_data', name='load_csv_data'),
    )
