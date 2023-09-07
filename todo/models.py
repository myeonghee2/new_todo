from django.db import models

# Create your models here.
class Todo(models.Model):
    class Meta:
        db_table = "todo"

    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)