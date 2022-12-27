from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='pictures')
    is_published = models.BooleanField()
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


class Categories(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"