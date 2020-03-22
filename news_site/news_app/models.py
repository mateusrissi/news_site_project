from djongo import models

'''class Category(models.TextChoices):
    tech = 'TC', 'Tecnology'
    general = 'GR', 'General'
    science = 'SC', 'Science'
    politics = 'PL', 'Politics'
'''


class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()
    active = models.BooleanField(default=True)
    img = models.ImageField(upload_to='posts', null=True, blank=True)
    '''
        categories = models.CharField(
            max_length=2,
            choices=Category.choices,
            default=Category.GR,
        )
    '''

    def __str__(self):
        return self.title
