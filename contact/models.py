from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
