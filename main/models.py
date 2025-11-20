from django.db import models

# Product
class Owner(models.Model):
    full_name = models.CharField(max_length=90, verbose_name="Full name")
    avatar = models.FileField(verbose_name="Аватар", upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.full_name
    



class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name="Product name")
    description = models.TextField(verbose_name="Description")
    cost = models.FloatField(verbose_name="Cost")
    rating = models.FloatField(verbose_name="Rating")
    owner = models.ForeignKey(Owner, on_delete = models.CASCADE)
    

    def __str__(self):
        return self.name + ": " + self.description
    






     


