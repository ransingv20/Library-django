
from django.shortcuts import render,HttpResponse,redirect
from .models import BookData
from django.http import HttpResponse
import csv
import os
# Create your views here.

def add_book(request):
    print(request.FILES)
    if request.method == "POST":
        print(request.POST)
        id = request.POST.get("id")
        name = request.POST.get("book_name")
        price = request.POST.get("book_price")
        quantity = request.POST.get("book_quantity")
        author = request.POST.get("book_author")
        is_published = request.POST.get("book_is_published")
        if is_published == "on":
            is_published = True
        else:
            is_published = False  
        try:      
            if not id:
                BookData.objects.create(name=name,price=price,quantity=quantity,author=author,is_published=is_published)
            else:      
            book_obj = BookData.objects.get(id=id)
            print(book_obj)
            book_obj.name = name
            book_obj.price = price
            book_obj.quantity = quantity
            book_obj.author = author
            book_obj.is_published = is_published
            book_obj.save()
        except     
        return redirect("home")
    else:
        return render(request,"home.html")


def display_books(request):
    print(BookData.objects.all())
    return render(request,"display_books.html",{"all_books" : BookData.objects.all()})      
    # paasing all_books to display_books.html page


def create_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="book.csv"'

    writer = csv.writer(response)
    writer.writerow(['name', 'price','quantity', 'author', 'is_published','is_active'])

    books = BookData.objects.all().values_list('name', 'price','quantity', 'author', 'is_published','is_active')
    for book in books:
        writer.writerow(book)
    return response


def upload_csv(request):
    pass

