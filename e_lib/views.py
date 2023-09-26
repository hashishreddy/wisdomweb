from django.shortcuts import render,redirect,get_object_or_404
from .forms import BookForm
from .models import Subject, Book

from django.contrib import messages
from django.contrib.auth.decorators import login_required




from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .models import ViewedBook
from django.utils import timezone

def home(request):
    
    if request.method == 'POST':
        
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('subject_list')
        else:
            messages.success(request,("Incorrect username or password,try again"))
            return redirect('home')

    else:   
        return render(request, 'home.html', {})
    

def search_book(request):
    if request.method == "POST":
        searched = request.POST['searched']
        Books = Book.objects.filter(books_name__contains=searched)
        return render(request,'search_book.html', {'searched':searched,'Books':Books})
    else:
        return render(request,'search_book.html',{})

def contact(request):
    
    
    return render(request,'contact.html',{})
# def books(request):
    

#     return render(request,'books.html',{})
# def books(request):
    
#     book_list = Book.objects.all()
#     return render(request,'books.html',{'book_list':book_list})


@login_required

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.added_by = request.user  # Assign the first_name to added_by
            form_instance.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})





def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subject_list.html', {'subjects': subjects})

def books_by_subject(request, subject_id):
    subject = get_object_or_404(Subject, subject_id=subject_id)
    books = Book.objects.filter(subject=subject)
    return render(request, 'books_by_subject.html', {'subject': subject, 'books': books})

def book_detail(request, books_id):
    book = get_object_or_404(Book, books_id=books_id)
    print(book)  # Check if the book object is populated
    context = {'book': book}
    return render(request, 'book_detail.html', context)

def view_pdf(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    
    viewed_book, created = ViewedBook.objects.get_or_create(user=request.user, book=book)
    if created:
        viewed_book.viewed_at = timezone.now()
        viewed_book.save()
    
    pdf_file_url = book.book_pdf.url
    return redirect(pdf_file_url)

def profile(request):
    return render(request, 'profile.html', {'user': request.user})


def my_activity(request):
    books = Book.objects.all()
    return render(request, 'my_activity.html',{'books': books})