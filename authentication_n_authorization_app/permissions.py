from rest_framework.permissions import BasePermission, SAFE_METHODS

# here we create custom/own permission class.
# Define our own Permission class which allows only SAFE_METHODS (GET,HEAD,OPTIONS)
class IsReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return False 

# here we allowed only get and patch method.     
class IsGetOrPatch(BasePermission):
    def has_permission(self, request, view):
        allowed_methods = ['GET', 'PATCH']
        if request.method in allowed_methods:
            return True
        else:
            return False

      
''' Define our own permission class with the following requirement:
- If the name is sunny then allow all methods
- If the name is not sunny and the name contains even number of characters then allow
- only safe methods otherwise not allowed to perform any operation ''' 
class SunnyPermission(BasePermission):
    def has_permission(self,request,view):
        username=request.user.username  # get authenticate user's name
        # if username is sunny then perform all operations
        if username.lower()=='sunny':   
            return True
        # username is not Empty & length of username must be even num & request method is must be SAFE_METHODS(Get, opetions, head).
        elif username != '' and len(username)%2 == 0 and request.method in SAFE_METHODS:   
            return True
        # otherwise user can not perform any operations. 
        else:
            return False  
        
