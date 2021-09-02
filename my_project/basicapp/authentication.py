#didnot use tis instead used it in views.py
from django.contrib.auth.models import User
class EmailAuthbackend(object):
    def authenticate(self,username=None,password=None):
        try:
            user=User.object.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None
    def get_user(self,user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
