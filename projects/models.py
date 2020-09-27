from django.db import models

class Projects(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/")
    summary = models.TextField(max_length=500)

    def __str__(self):
        return self.summary
    