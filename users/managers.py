from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, password = None):
        user = self.model(username = username)
        user.is_active = True
        user.set_password(password)
        user.save(using = self._db)
        return user
    

    def create_superuser(self, username, password):
        user = self.create_user(username, password)
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using = self._db)
        return user