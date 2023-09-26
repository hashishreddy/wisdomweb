from django.urls import path
from.import views
urlpatterns = [
    path('',views.home,name="home"),
    path('contact/',views.contact,name="contact"),  
    path('add_book/',views.add_book, name="add_book"),
    path('subjects/', views.subject_list, name='subject_list'), 
    path('books/<int:subject_id>/', views.books_by_subject, name='books_by_subject'),
    path('book/<int:books_id>/', views.book_detail, name='book_detail'),
    path('search_book/', views.search_book, name='search_book'), 
    path('view-pdf/<int:book_id>/', views.view_pdf, name='view_pdf'),
    path('profile/', views.profile, name='profile'), 
   
    path('my_activity/', views.my_activity, name='my_activity'), 
]