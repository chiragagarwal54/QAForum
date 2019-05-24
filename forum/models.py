from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

class question(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    #refer https://stackoverflow.com/questions/38388423/what-does-on-delete-do-on-django-models
    #refer https://stackoverflow.com/questions/8609192/differentiate-null-true-blank-true-in-django
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    created_on = models.DateTimeField(auto_now=True)
    last_updated_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title

class answer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(question, on_delete=models.CASCADE)
    answer_text = models.TextField()
    is_anonymous = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text
