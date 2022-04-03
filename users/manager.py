from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):
    # Jika ada _ (underscore) di depan code artinya privat ga bisa benear2 di gunakan tanpa metode lain
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        # untuk validasi email
        if not email:
            raise ValueError('User Must Have Email ')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )

        # set password
        user.set_password(password)
        user.save(using=self.db)
        return user

    # Create New User
    def create_user(self, email, password, **extra_fields):
        return self.create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        user.save(using=self._db)
        return user
