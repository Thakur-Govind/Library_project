from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.contrib.auth import authenticate, login
from django.shortcuts import render,get_object_or_404
# Create your views here.
from . import models

class BookListView(ListView):
    model = models.Book
    template_name = 'book_list.html'

"""def logIn(request):
    uname = request.POST.get('username',False)
    passw = request.POST.get('password',False)
    acc_no = request.POST.get('acc_no',False)
    message = ""
    result = authenticate(request,username = uname, password = passw)
    if result:
        login(request,result)
        message = "Login Successfull!!!!"
        acc = get_object_or_404(models.account, pk = acc_no)
        book_issued = models.Book.filter(account= acc) #getting the books linked to account

        return render(request, 'books/book_list.html',{'uname': uname, 'mess':message ,'books_issued' : book_issued} )
    else:
        message = "Login failed, please try again"
        return render(request, 'books/login.html', {'mess':message})"""
def addbook(request):
    if 'addbook' in request.POST:
        n_b = models.Book()
        n_b.title = request.POST.get('title',False)
        n_b.subtitle = request.POST.get('subtitle',False)
        n_b.author = request.POST.get('author',False)
        n_b.isbn = request.POST.get('isbn',False)
        n_b.save()
    elif 'rembook' in request.POST:
        book = get_object_or_404(models.Book, pk = request.POST.get('title',False))
        book.delete()
    return redirect('home')
def create(request):
    return render(request, 'books/create_book.html')
def bookdetail(request, bookt):
    book = get_object_or_404(models.Book, pk=bookt)
    return render(request, 'books/bookdetails.html',{'model':book})
def updatebook(request, bookt):
    n_b = get_object_or_404(models.Book, pk = bookt)
    n_b.subtitle = request.POST.get('subtitle',False)
    n_b.author = request.POST.get('author',False)
    n_b.isbn = request.POST.get('isbn',False)
    n_b.save()
    return redirect('home')
def update(request,bookt):
    return render(request, 'books/editbook.html',{'book':get_object_or_404(models.Book, pk = bookt)})
