from django.contrib.auth.models import AbstractUser
from django.db.models import CharField{% if cookiecutter.username_type == "email" %}, EmailField{% endif %}
from django.urls import reverse
{%- if cookiecutter.username_type == "email" %}

from apps.users.managers import UserManager
{% endif %}

class User(AbstractUser):
    """
    Default custom user model for Email as Username.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    preferred_name = CharField(
        "Preferred/Nickname", blank=True, null=True, max_length=255
    )
    {%- if cookiecutter.username_type == "email" %}
    email = EmailField("email address", unique=True)
    username = None  # type: ignore

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()
    {% endif %}

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        {%- if cookiecutter.username_type == "email" %}
        return reverse("users:detail", kwargs={"pk": self.id})
        {%- else %}
        return reverse("users:detail", kwargs={"username": self.username})
        {%- endif %}
    
    def __str__(self) -> str:
        if self.preferred_name:
            return self.preferred_name
        elif self.first_name:
            return self.first_name
        else:
            return self.email
