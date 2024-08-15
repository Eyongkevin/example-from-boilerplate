from django.db import models
from django.contrib.postgres.fields import IntegerRangeField
from django.contrib.postgres.validators import RangeMinValueValidator, RangeMaxValueValidator
# from django.db.backends.postgresql.psycopg_any import NumericRange

# Create your models here.

class MyRead(models.Model):
    book_isbn = models.ForeignKey('book.Book', on_delete=models.CASCADE)
    reader_username = models.ForeignKey('reader.Reader', on_delete=models.CASCADE)
    # PositiveIntegerField already adds a Check with the name
    # app_label_class_fieldname_check
    # myread_myread_percentage_read_check
    percentage_read = models.PositiveSmallIntegerField(null=True, blank=True)
    start_read_date = models.DateField(null=True, blank=True)
    end_read_date = models.DateField(null=True, blank=True)

    class Meta:
        constraints = [
            # models.UniqueConstraint(fields=['app_uuid', 'version_code'], name='unique appversion')
            models.CheckConstraint(
                name='%(app_label)s_%(class)s_per_read_check',
                check=models.Q(
                    percentage_read__gte=0,
                    percentage_read__lte=100
                    )
            ),
            models.CheckConstraint(
                name='%(app_label)s_%(class)s_end_start_read_check',
                check=models.Q(
                    end_read_date__gt=models.F('start_read_date')
                )
            ),
            models.CheckConstraint(
                name='%(app_label)s_%(class)s_percentage_read_start_read_check',
                check=(
                    models.Q(
                        percentage_read__exact=0,
                        start_read_date__isnull=True
                    )
                    | models.Q(
                        percentage_read__gt=0,
                        start_read_date__isnull=False
                    )
                )

            ),
            models.CheckConstraint(
                name='%(app_label)s_%(class)s_percentage_read_end_read_check',
                check=(
                    models.Q(
                        percentage_read__exact=100,
                        end_read_date__isnull=False
                    )
                    | models.Q(
                        percentage_read__lt=100,
                        end_read_date__isnull=True
                    )
                )

            )
        ]

    def __str__(self) -> str:
        return f'{self.reader_username} -> {self.book_isbn}'


class StatusPercent(models.Model):
    percentage_read_range = IntegerRangeField(
        #default=NumericRange(1, 101),
        blank=True,
        validators=[
            RangeMinValueValidator(0),
            RangeMaxValueValidator(101)
        ]
    )
    read_status = models.CharField(max_length=10)

    class Meta:
        constraints = [
            # models.UniqueConstraint(fields=['app_uuid', 'version_code'], name='unique appversion')
            models.CheckConstraint(
                name='%(app_label)s_%(class)s_read_status_check',
                check=models.Q(
                    read_status__in=['pending', 'reading', 'done']
                    )
            )
        ]

    def __str__(self) -> str:
        return f'{self.percentage_read_range}({self.read_status})'