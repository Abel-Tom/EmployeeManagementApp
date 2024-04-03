from django.db import models

from zelthy.apps.appauth.models import UserRoleModel
from zelthy.apps.dynamic_models.models import DynamicModelBase
from zelthy.apps.dynamic_models.fields import ZOneToOneField
from zelthy.core.storage_utils import ZFileField


class LoginConfigModel(DynamicModelBase):
    user_role = ZOneToOneField(
        UserRoleModel,
        on_delete=models.PROTECT,
        related_name="login_config",
        help_text="User Role",
    )
    config = models.JSONField(default=dict, help_text="User Role based Login Config")

    def __str__(self):
        return f"LoginConfigModel - {self.user_role.name}"


class GenericLoginConfigModel(DynamicModelBase):
    config = models.JSONField(default=dict, help_text="Generic Login Config")
    logo = ZFileField(blank=True, null=True)
    background_image = ZFileField(blank=True, null=True)

    def __str__(self):
        return f"GenericLoginConfigModel - {self.id}"
