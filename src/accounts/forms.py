from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from django.forms import EmailField, EmailInput, ModelForm

from accounts.models import Profile


class RegistrationForm(UserCreationForm):
    email = EmailField(widget=EmailInput(attrs={"required": "True"}))

    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email", "password1", "password2"]

    def clean(self):
        cleaned_data = super().clean()

        if not bool(cleaned_data["email"]):
            raise ValidationError("Insert email address.")
        if get_user_model().objects.filter(email=cleaned_data["email"]).exists():
            raise ValidationError("User with this email already exists.")


class UserProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["avatar"]

    def clean_avatar(self):
        avatar = self.cleaned_data["avatar"]

        try:
            w, h = get_image_dimensions(avatar)

            # validate dimensions
            max_width = max_height = 100
            if w > max_width or h > max_height:
                raise ValidationError(
                    "Please use an image that is " "%s x %s pixels or smaller." % (max_width, max_height)
                )

            # validate content type
            main, sub = avatar.content_type.split("/")
            if main != "image" or sub not in ["jpeg", "jpg", "png"]:
                raise ValidationError("Please use a JPEG, JPG or PNG image.")

            # validate file size
            if len(avatar) > (20 * 1024):
                raise ValidationError("Avatar file size may not exceed 20k.")

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
        return avatar
