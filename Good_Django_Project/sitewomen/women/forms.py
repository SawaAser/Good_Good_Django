from django import forms
from .models import Category, Husband
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError
from .models import Women

# @deconstructible
# class UaValidator:
#     ALLOWED_CHARS = 'йцукенгшщзхфівапролджєячсмитьбю.ЙЦУКЕНГШЩЗХЇФІВАПРОЛДЖЄЯЧСМИТЬБЮ.1234567890- '
#     code = 'ua'
#
#     def __init__(self, message=None):
#         self.message = message if message else "повинні бути присутні тільки українські букви"
#
#     def __call__(self, value, *args, **kwargs):
#         if not (set(value) <= set(self.ALLOWED_CHARS)):
#             raise ValidationError(self.message, code=self.code)


class AddPostForm(forms.ModelForm):

    cat = forms.ModelChoiceField(queryset=Category.objects.all(),
                                 empty_label='не вибрано',
                                 label='Категорії'
                                 )
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(),
                                     required=False,
                                     empty_label="не заміжня",
                                     label='Чоловік'
                                     )

    class Meta:
        model = Women
        # fields = '__all__' # Всі крім тих які заповнються автоматично
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat', 'husband', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }
        labels = {
            'slug': 'URL'
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError('Довжина перевищює 50 символів')

        return title


class UploadFileForm(forms.Form):
    file = forms.ImageField(label='Файл')
