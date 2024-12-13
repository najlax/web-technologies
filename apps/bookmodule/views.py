from django.http import HttpResponse
from django.shortcuts import render
from .models import Book 
from django.db.models import Q 
from django.db.models import Sum, Avg , Min, Max

def index(request):
 name = request.GET.get("name") or "world!"
 return render(request, "index.html" , {"name": name})

def index2(request, val1 = 0): #add the view function (index2)
 return HttpResponse("value1 = "+str(val1))

mybook = Book(title = 'Continuous Delivery', author = 'J.Humble and D. Farley', edition = 1)


def viewbook(request, bookId):
  # assume that we have the following books somewhere (e.g. database) 
  book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'} 
  book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'} 
  targetBook = None 
  if book1['id'] == bookId: targetBook = book1 
  if book2['id'] == bookId: targetBook = book2 
  context = {'book':targetBook} # book is the variable name accessible by the template 
  return render(request, 'show.html', context) 

def links(request):
 return render(request, "links.html")

def formatting(request):
 return render(request,"formatting.html")

def listing(request):
 return render(request, "listing.html")

def tables(request):
 return render(request, "table.html")

def index(request):
 return render(request,"bookmodule/index.html")

def books(request):
 return render(request,"bookmodule/bookList.html")

def viewbook(request):
 return render(request,"bookmodule/one_book.html")

def aboutus(request):
 return render(request,"bookmodule/aboutus.html")

def search(request):
 return render(request, "bookmodule/search.html")



  


def search_books(request):
    if request.method == "POST":
        keyword = request.POST.get('keyword').lower()
        search_title = request.POST.get('option1')
        search_author = request.POST.get('option2')

        # Filter books
        books = __getBooksList()
        filtered_books = []
        for book in books:
            found = False
            if search_title and keyword in book['title'].lower():
                found = True
            if not found and search_author and keyword in book['author'].lower():
                found = True
            if found:
                filtered_books.append(book)

        return render(request, 'bookmodule/bookList.html', {'books': filtered_books})
    return render(request, 'bookmodule/search.html')


def simple_query(request):
  mybooks =Book.objects.filter(title__icontains='and') # <- multiple objects
  return render(request, 'bookmodule/bookList.html', {'books':mybooks})


def lookup_query(request): 
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10] 
    if len(mybooks)>=1: 
     return render(request, 'bookmodule/bookList.html', {'books':mybooks}) 
    else: 
     return render(request, 'bookmodule/index.html') 
    
def lab8t1(request):
  mybooks=Book.objects.filter(Q(price__lte=50))
  return render(request,'bookmodule/bookList.html', {'books':mybooks})

def lab8t2(request):
  mybooks=Book.objects.filter(Q(edition__gt=2) & (Q(title__contains="qu") | Q(author__contains="qu")))
  return render(request, 'bookmodule/bookList.html', {'books': mybooks})
        
def lab8t3(request):
  mybooks=Book.objects.filter(~Q(edition__gt=2) & (~Q(title__contains="qu") | ~Q(author__contains="qu")))
  return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def lab8t4(request):
  mybooks=Book.objects.all().order_by('title')
  return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def lab8t5(request):
  mybooks=Book.objects.all().count()
  totalprice=Book.objects.aaggregate(total=Sum('price'))
  avgprice=Book.objects.aaggregate(averagep=Avg('price'))
  Minprice=Book.objects.aaggregate(min=Min('price'))
  Maxprice=Book.objects.aaggregate(max=Max('price'))


