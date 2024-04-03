from django.contrib.auth import get_user_model
from django.db import models



# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = "Categories"
        db_table = 'categories'


class News(models.Model):
    news_title = models.CharField(max_length=255, unique=True)
    news_description = models.CharField(max_length=255)
    news_image = models.ImageField(upload_to='news/')
    news_content = models.TextField()
    news_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    news_pub_date = models.DateTimeField(auto_now_add=True)
    news_author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.news_title

    class Meta:
        verbose_name_plural = "News"
        db_table = 'news'


class Xabar(models.Model):
    mavzu = models.CharField(max_length=200)
    matn = models.TextField()


# class CustomUser(AbstractUser):
#     global Entite1
#     username = None
#     email = models.EmailField()
#     profil = models.CharField(max_length=10, unique=True)
#     is_profil_verified = models.BooleanField(default=False)
#     Entite1 = models.ForeignKey(Entite1, on_delete=models.CASCADE, related_name='entite', blank=True, null=True)
#
#     objects = UserManager()
#
#     USERNAME_FIELD = 'profil'
#     REQUIRED_FIELDS = []