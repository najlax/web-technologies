from django.urls import path
from . import views
urlpatterns = [
 path('', views.index, name= "books.index"),
 path('index2/<int:val1>/', views.index2),
 path('<int:bookId>', views.viewbook),
 path('html5/links/', views.links),
 path('html5/text/formatting/', views.formatting),
 path('html5/listing/', views.listing),
 path('html5/tables/', views.tables),
 path('list_books/', views.books, name="books.list_books"),
 path('aboutus/', views.aboutus, name="books.aboutus"),
 path('list_books/one_book/',views.viewbook),
 path('search/', views.search_books),
 path('simple/query/', views.simple_query),
 path('complex/query/', views.lookup_query),
 path('lab8/task1/', views.lab8t1),
 path('lab8/task2',views.lab8t2),
 path('lab8/task3/',views.lab8t3),
 path('lab8/task4/', views.lab8t4),
 path('lab8/task5/', views.lab8t5),
]
