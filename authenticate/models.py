from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class PasswordReset(models.Model):
    user = models.ForeignKey( User, on_delete = models.CASCADE )
    reset_id = models.UUIDField( unique = True, editable = True, default = uuid.uuid4 )
    created_at = models.DateTimeField( auto_now_add = True )
    
    def __str__(self):
        return f"The Password Reset is generated for the user {self.user.username} at {self.created_at}"
    
    class Meta:
        verbose_name_plural = 'Password Reset'