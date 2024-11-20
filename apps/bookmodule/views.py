from django.http import HttpResponse
from django.shortcuts import render

def index(request):
 name = request.GET.get("name") or "world!"
 return render(request, "index.html" , {"name": name})

def index2(request, val1 = 0): #add the view function (index2)
 return HttpResponse("value1 = "+str(val1))

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

def list_books(request):
 return render(request,"bookmodule/list_books.html")

def viewbook(request):
 return render(request,"bookmodule/one_book.html")

def aboutus(request):
 return render(request,"bookmodule/aboutus.html")

def search(request):
 return render(request, "bookmodule/search.html")


def __getBooksList(): 
  book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'} 
  book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'} 
  book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'} 
  return [book1, book2, book3] 

  


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
