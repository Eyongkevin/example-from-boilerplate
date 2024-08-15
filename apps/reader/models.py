from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import timedelta
# Create your models here.


class NIC(models.Model):
    id_number = models.CharField(max_length=10, primary_key=True)
    delivery_date = models.DateField()
    #expiration_date = delivery_date + 5 years
    expiration_date = models.GeneratedField(
        expression = models.F('delivery_date') + timedelta(days=1826.25),
        output_field = models.DateField(),
        db_persist = True
    )

    def __str__(self) -> str:
        return f'{self.id_number}(del: {self.delivery_date} , exp: {self.expiration_date})'

    class Meta:
        db_table_comment = 'National Identity Card'
        get_latest_by = ['delivery_date', '-expiration_date']


class Reader(AbstractUser):
    # class TitleChoice(models.TextChoices): # TitleChoice.choices
    #     Mr = 'Mr'
    #     Mrs = 'Mrs'
    #     Dr = 'Dr'
    READER_TITLE ={
        'Mr': 'Mr',
        'Mrs': 'Mrs',
        'Dr': 'Dr'
    }

    id = None 
    username = models.CharField(max_length=50, unique=True, primary_key=True, help_text='Reader username')
    title = models.CharField(max_length=5, choices= READER_TITLE, null=True, blank=True)
    nic = models.OneToOneField(NIC, on_delete=models.CASCADE, null=True, blank=True)
    # related_name='reader'
    class Meta:
        default_related_name = '%(app_label)s_%(model_name)s'
        constraints = [
            models.CheckConstraint(
                name='%(app_label)s_%(class)s_title_check',
                check=models.Q(title__in=['Mr', 'Mrs', 'Dr'])
                )
        ]

    def __str__(self) -> str:
        return f'{self.username}'