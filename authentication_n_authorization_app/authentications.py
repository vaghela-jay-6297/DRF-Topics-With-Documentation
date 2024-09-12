from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User

# create custom authentication
class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.GET.get('username')  # get username from query string(url)
        if username is None:    # check username is None or not?
            return None # if None than return None
        try:
            user = User.objects.get(username=username)  # get user object from DB
        except User.DoesNotExist:   # user not exist exception found
            raise AuthenticationFailed("No Such type of user.") # raise exception
        return (user, None) # return tuple with user object and None
    

'''
1) Client required to send secret key and username as query parameters.
2) Length of key should be 7 characters
3) The first character should be lower case alphabet symbol which should be last
character of username
4) The third character should be 'Z'
5) The 5 th character should be first character of username

Eg:
username: durga
secrete key: a7ZXd98
'''
class CustomAuthentication2(BaseAuthentication):
    def authenticate(self, request):
        username = request.GET.get('username')  # get username from query string(url)
        key = request.GET.get('key')    # get key from query string(url)
        # check username or key is None than return None.
        if (username is None) or (key is None):
            return None
        
        # conditions (return response in True/False of below condition)
        c1 = len(key) == 7  # Length of key should be 7 characters 
        c2 = key[0] == username[-1].lower() # The first character should be lower case alphabet symbol which should be last character of username
        c3 = key[2] == 'Z'  # The third character should be 'Z'
        c4 = key[4] == username[0]  # The 5 th character should be first character of username

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed("Your provided username is invalid, please provide valid username to access endpoint.")
        
        # if user exist
        if c1 and c2 and c3 and c4: # all condition are True than execute return statement
            return (user, None)
        else:   # when condtions are false
            raise AuthenticationFailed("Your provided secret key is invalid, please provide valid secret key to access endpoint.")



