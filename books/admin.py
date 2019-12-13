from django.contrib import admin
from .models import Book,account,issued_by

admin.site.register(Book)
admin.site.register(account)
admin.site.register(issued_by)

# Register your models here.
