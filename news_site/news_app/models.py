from djongo import models


class Author(models.Model):
    name = models.CharField(db_index=True, max_length=150, primary_key=True)
    email = models.EmailField(default=None)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(db_index=True,max_length=150, primary_key=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(db_index=True,max_length=100, unique=True)
    sub_title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'Author', on_delete=models.CASCADE, default="Mateus")
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, default="General")
    content = models.TextField()
    published = models.BooleanField(default=True)
    img = models.ImageField(upload_to='posts', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
