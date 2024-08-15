from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Book
from .forms import PostBookForm

@login_required
def book_detail(request, isbn: str):
    book = Book.objects.get(pk=isbn)
     # set max viewed resources to store
    max_viewed_books = 5
    # Get current value of the stored viewed resources if any, else return []
    viewed_books = request.session.get('viewed_books', [])
    
    # create the list to be stored in the session
    viewed_book = [book.isbn, book.title]
    
    # remove it if it already exist. This is because we want it to be append at the start of the list
    if viewed_book in viewed_books:
        viewed_books.remove(viewed_book)
        
    # insert at index 0
    viewed_books.insert(0, viewed_book)

    # Get the limit
    viewed_books = viewed_books[:max_viewed_books]
    
    # add it back to our session
    request.session['viewed_books'] = viewed_books
 
    # TODO: List all authors and tags
    context = {
        'book': book,
        'tags': ', '.join(tag.name for tag in book.tags.all()),
        'authors': ', '.join([author.first_name + ' '+ author.last_name for author in book.authors.all()])}
    return render(request, 'book_detail.html', context)


# def book_post(request):
#     # TODO: process the form here
#     breakpoint()

#     return render(request, 'post.html')

def book_post(request):
    # Unbound, # user made a GET request
    if request.method == "GET":
        form = PostBookForm()
        return render(
            request,
            "book_post.html",
            {"form": form},
        )
    else:
        # Bound # user made a POST request
        # info = {"title": "kevin", "link": "http:hello", "description": "hello"}
        form = PostBookForm(request.POST)
        # form = PostResourceForm(info)

        # validation
        # .is_valid() method
        # .cleaned_data attribute
        if form.is_valid():
            data = form.cleaned_data
            # TODO: Save it to the database
            # TODO: Redirect the user to the home page
        else:
            pass