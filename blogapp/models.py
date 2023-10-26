from django.db import models
from django.urls import reverse

# Create class Category.
class Category(models.Model):
    category_name = models.CharField(max_length=25)

# Create class Post.
class Post(models.Model):
    post_header = models.CharField(max_length=50)
    post_text = models.TextField()
    post_author = models.CharField(max_length=50)
    post_datatime = models.DateTimeField()
    category = models.ForeignKey(Category,on_delete=models.SET_DEFAULT, default="no category")
    image = models.ImageField(upload_to="images/", default=None, null=True)

    def get_absolute_url(self):
        return reverse("post-details", args=[str(self.id)]) 
