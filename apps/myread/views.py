from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.db.models import Count
from .models import MyRead
from apps.reader.models import Reader
from apps.book.models import Book
from .utils import generate_book_cat_count_list

#from . import models

# Create your views here.
# def home_page(request): # HttpRequest
#     response = """
#     <html>
#         <h1>
#             Welcome to My Read App
#         </h1>
#     </html>"""

#     return HttpResponse(response) # HttpResponse

# def home_page(request):
#     from . import models

#     reader_cnt = models.MyRead.objects.distinct('reader_username').count()
#     response = f"""
#       <html>
#          <h1>Welcome to My Read App</h1>
         
#          <p>{reader_cnt} engaged reader{'s' if reader_cnt > 1 else ''} and counting!</p>
#       </html>
#     """
#     return HttpResponse(response) 

# Create your views here.
def home_page(request):
    reader_cnt = Reader.objects.all().count()
    engaged_reader_cnt = MyRead.objects.distinct('reader_username').count()
    cnt_per_cat = Book.objects.values("category").annotate(cnt=Count("*"))
    books = Book.objects.all()
    #book_cnt = Book.objects.count()
    # cnt_per_cat = Resources.objects.select_related('cat_id').annotate(cnt=Count("cat_id")).values("cnt", 'cat_id__cat')

    context = {
        'reader_cnt': reader_cnt,
        'engaged_reader_cnt': engaged_reader_cnt,
        'cnt_per_cat': cnt_per_cat,
        'book_cnt': len(books),
        'books': books
    }

    return render(request, 'home_page.html', context)
class HomePage(TemplateView):
    template_name = 'home_page.html'