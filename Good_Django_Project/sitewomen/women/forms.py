from django import forms
from .models import Category, Husband
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError


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


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255,
                            min_length=5,
                            label='Заголовок',
                            widget=forms.TextInput(attrs={'class': 'form-input'}), # тут типу додатвові параметри прописуємо до html
                            # validators=[
                            #     UaValidator(),          # остут ми додаємо свій валідатор
                            # ],
                            error_messages={
                                'min_length': 'Занадто коротко',
                                'required': 'Без заголовка'
                            })
    slug = forms.SlugField(max_length=255, label='URL',
                           validators=[
                               MinLengthValidator(5, message='Мінімум 5 символів'),
                               MaxLengthValidator(100, message='Максимум 5 символів'),
                           ])
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}),
                              required=False,
                              label='Контент'
                              )
    is_published = forms.BooleanField(required=False,
                                      initial=True,
                                      label='Статус'
                                      )
    cat = forms.ModelChoiceField(queryset=Category.objects.all(),
                                 empty_label='не вибрано',
                                 label='Категорії'
                                 )
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(),
                                     required=False,
                                     empty_label="не заміжня",
                                     label='Чоловік'
                                     )

    def clea_title(self):  # други варіант валідатора
        title = self.cleaned_data['title']
        ALLOWED_CHARS = 'йцукенгшщзхфівапролджєячсмитьбю.ЙЦУКЕНГШЩЗХЇФІВАПРОЛДЖЄЯЧСМИТЬБЮ.1234567890- '

        if not (set(title) <= set(ALLOWED_CHARS)):
            raise ValidationError("повинні бути присутні тільки українські букви")
