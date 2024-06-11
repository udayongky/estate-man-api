import uuid

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.users.managers import UserManager


class UsernameValidator(validators.RegexValidator):
    regex = r"^[\w.@+-]+\Z"
    message = _(
        "Your username is not valid. A username can only contain letters, numbers, a dot, @ symbol, + symbol and a hyphen"  # noqa: E501
    )
    flag = 0


class User(AbstractUser):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(verbose_name=_("First Name"), max_length=60)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=60)
    email = models.CharField(verbose_name=_("Email Address"), unique=True, db_index=True)
    username = models.CharField(verbose_name=_("Username"), max_length=60, unique=True, validators=[UsernameValidator])

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["-date_joined"]

    @property
    def get_full_name(self) -> str:
        full_name = f"{self.firs_name} {self.last_name}"
        return full_name.strip()

    # groups = models.ManyToManyField(
    #     Group,
    #     related_name="custom_user_set",  # Avoids clash with auth.User.groups
    #     blank=True,
    #     help_text=_(
    #         "The groups this user belongs to. A user will get all permissions granted to each of their groups."
    #     ),
    #     related_query_name="user",
    # )
    # user_permissions = models.ManyToManyField(
    #     Permission,
    #     related_name="custom_user_set",  # Avoids clash with auth.User.user_permissions
    #     blank=True,
    #     help_text="Specific permissions for this user.",
    #     related_query_name="user",
    # )
