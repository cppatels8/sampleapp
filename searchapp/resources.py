from tastypie.resources import ModelResource, ALL
from tastypie.authentication import BasicAuthentication
from custom_authorization import CustomAuthorization

from models import MPattendence

class MPattendenceResource(ModelResource):
    class Meta:
        queryset = MPattendence.objects.all()
        dispatch_list_methods= ['get', 'post']
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'mpattendence'
        authentication = BasicAuthentication()
        authorization = CustomAuthorization()
        filtering = {
                     "member_name": ALL,
                     "id": ALL,
                     "lok_sabha": ALL
                }
