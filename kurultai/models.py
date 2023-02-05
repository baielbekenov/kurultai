from django.contrib.auth.models import AbstractUser
from django.db import models

STATUS = ((0, "Draft"), (1, "Publish"))
class Account(AbstractUser):
    is_tor_aga = models.BooleanField(verbose_name='Тор Ага', default=False)
    is_zam = models.BooleanField(verbose_name='Заместитель Тор Ага', default=False)
    is_katchy = models.BooleanField(verbose_name='Катчы', default=False)
    is_delegat = models.BooleanField(verbose_name='Делегат', default=False)

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.get_full_name()


class Rubrics(models.Model):
    title = models.CharField(max_length=24, verbose_name='Название рубрики')
    content = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="blog_posts")
    rubric_id = models.ForeignKey(Rubrics, on_delete=models.CASCADE, verbose_name='Рубрика')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False, verbose_name='Active')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)






