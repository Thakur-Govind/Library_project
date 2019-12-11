from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=250, primary_key=True)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    #accounts = models.ForeignKey('account', on_delete = models.CASCADE, default=None )

    #def __str__(self):
    #    return self.title

""""class account(models.Model):
    name = models.CharField(max_length = 100)
    account_no = models.CharField(max_length  =10, primary_key = True)
    no_books_issued= models.IntegerField(default = 0)
"""
