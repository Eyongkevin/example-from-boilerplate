from django import forms

# TODO: Add fields for category(Radio) and tags(Select)

# Testing this


class PostBookForm(forms.Form):
    BOOK_CATEGORY = {
        "pr":"programming",
        "ar": "art",
        "hi": "history",
        "po": "politics",
        "ot": "other"
    }
    isbn = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "isbn-input",
                "placeholder": "Enter a isbn",
            }
        )
    )  # type='text'
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "title-input",
                "placeholder": "Enter a title",
            }
        )
    )  # type='text'
    pages = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "pages-input",
                "placeholder": "Enter pages",
            }
        )
    )  # type='text'
    description = forms.CharField(widget=forms.Textarea)  # type='textarea'
    category = forms.ChoiceField(
        widget=forms.RadioSelect(
            attrs={
                "class": "form-cat"
            }
        ), 
        choices=BOOK_CATEGORY)