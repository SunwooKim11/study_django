from django.db import models

# Create your models here.
class Feed(models.Model):
    content_text= models.TextField()
    user_id = models.TextField()
    user_image = models.TextField()
    content_image = models.TextField()
    like_count = models.IntegerField()

    def contents(self):
        return [self.content_text, self.user_id, self.user_image,
                self.content_image, self.like_count]

class Recommend(models.Model):
    user_id = models.TextField()
    user_info = models.TextField()
    user_image = models.TextField()

    def contents(self):
        return [self.user_id, self.user_info, self.user_image]