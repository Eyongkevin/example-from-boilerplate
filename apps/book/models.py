from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class BookManager(models.Manager):
    def filter_books_by_tags(self, *tags):
        return self.filter(tags__name__in=tags)

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
class AuthorsBooks(models.Model):
    AUTHOR_BOOK_ROLE = {
        "author": "Author",
        "co_author": "Co-Author",
        "editor": "Editor"
    }
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey('book.Book', on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=AUTHOR_BOOK_ROLE, default='author')

    def __str__(self) -> str:
        return f'{self.author}({self.role}) -> {self.book}'

    class Meta:
        verbose_name = 'Author and Book'
        verbose_name_plural = 'Authors and Books'


class Book(models.Model): # ('programming', 'art', 'history', 'politics', 'other')
    BOOK_CATEGORY = {
        "pr":"programming",
        "ar": "art",
        "hi": "history",
        "po": "politics",
        "ot": "other"
    }
    BOOK_FORMAT = {
        "eb": "ebook",
        "hc": "hardcover"
    }
    # When a primary key is not explicitly used, it then create the id
    #id = None 
    isbn = models.CharField(max_length=13, primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    page_count = models.IntegerField()
    category = models.CharField(max_length=2, choices=BOOK_CATEGORY, default="pr")
    published_date = models.PositiveSmallIntegerField()
    publisher = models.CharField(max_length=50)
    #authors = ArrayField(ArrayField(models.CharField(50)))
    authors = models.ManyToManyField(Author, through=AuthorsBooks)
    lang = models.CharField(max_length=50)
    edition = models.PositiveSmallIntegerField(null=True, blank=True)
    format = models.CharField(max_length=2, choices=BOOK_FORMAT, default='eb')
    tags = models.ManyToManyField('book.Tag')

    # Override objects
    objects = BookManager()

    def __str__(self) -> str:
        return f"{self.title}({self.isbn})"

    @property
    def short_des(self):
        return f'{self.description[:30]}...'

    @classmethod
    def get_books_by_tags(cls, *tags):
        return cls.objects.filter(tags__name__in=tags)
    
    class Meta:
        ordering = ('title',)



class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    # class Meta:
    #     constraints = [
    #         models.CheckConstraint(
    #              name='%(app_label)s_%(class)s_name_check',
    #              check=~models.Q(name__iexact=models.F('name'))
    #         )
    #     ]

    def __str__(self) -> str:
        return self.name
