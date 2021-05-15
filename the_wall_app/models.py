from django.db import models
from login_registration_app.models import *

# Create your models here.
class LengthValidator(models.Manager):
    def message_validator(self, postData):
        errors = {}

        if len(postData['message']) == 0:
            errors['message'] = "Can't post an empty message"

        return errors

    def comment_validator(self, postData):
        errors = {}

        if len(postData['comment']) == 0:
            errors['comment'] = "Can't post an empty message"

        return errors

class Message(models.Model):
    user = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    message = models.TextField()
    objects = LengthValidator()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    message = models.ForeignKey(Message, related_name="comments", on_delete=models.CASCADE)
    comment = models.TextField()
    objects = LengthValidator()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)