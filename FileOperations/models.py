from django.db import models

# class Book(models.Model):
#     name = models.CharField(max_length=200,null=True,unique=True)
#     price = models.FloatField(null=True)
#     qty = models.IntegerField(null=True)
#     author = models.CharField(max_length=200,null=True)
#     is_published = models.BooleanField(default=True,null=True)
#     is_active = models.BooleanField(default=True,null=True)

#     def __str__(self):
#         return f"{self.name}"

#     class Meta:
#         db_table = "library"    

class BookData(models.Model):
    name = models.CharField(max_length=250,null=True,unique=True)
    author = models.CharField(max_length=210,null=True)
    quantity = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    is_published = models.BooleanField(default=True,null=True)
    is_active = models.BooleanField(default=True,null=True)


    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "book_data"
