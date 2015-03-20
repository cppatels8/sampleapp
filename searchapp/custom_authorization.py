from tastypie.exceptions import Unauthorized
from tastypie.authorization import Authorization

class CustomAuthorization(Authorization):
    def read_list(self, object_list, bundle):
        if bundle.request.user.is_active and bundle.request.user.is_superuser:
            return  object_list
        return object_list.filter(user__id=bundle.request.user.id)
    
    def read_detail(self, object_list, bundle):
        if bundle.request.user.is_active and bundle.request.user.is_superuser:
            return  True
        return bundle.obj.id == bundle.request.user.id

    def create_list(self, object_list, bundle):
        raise Unauthorized("creating new users are not supported.")
    
    def create_detail(self, object_list, bundle):
        return True
#         raise Unauthorized("creating new users are not supported.")
    
    def update_list(self, object_list, bundle):
        raise Unauthorized("updates on this resource are not supported.")
    
    def update_detail(self, object_list, bundle):
        return True
        raise Unauthorized("updates on this resource are not supported.")
    
    def delete_list(self, object_list, bundle):
        raise Unauthorized("deletes on this resource are not supported.")
    
    def delete_detail(self, object_list, bundle):
        return True
        raise Unauthorized("deletes on this resource are not supported.")
   
   
   