from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.core.validators import MinLengthValidator, MaxLengthValidator


def translit_to_eng(s: str) -> str:
    d = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
         'е': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i', 'к': 'k',
         'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
         'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch',
         'ш': 'sh', 'щ': 'shch', 'ь': '', 'і': 'y', 'ъ': '', 'є': 'y', 'ю': 'yu', 'я': 'ya'}

    return "".join(map(lambda x: d[x] if d.get(x, False) else x, s.lower()))


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Women.Status.PUBLISHED)


class Women(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, "Чорновик"
        PUBLISHED = 1, "Опублікований"

    title = models.CharField(max_length=255, verbose_name='Загаловок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг',
                            validators=[
                                MinLengthValidator(5, message='Мінімум 5 символів'),
                                MaxLengthValidator(100, message='Максимум 5 символів'),
                            ])
    content = models.TextField(blank=True, verbose_name="Текст статї")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Час створення')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Час зміни')
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name='Опубліковано')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts', verbose_name='Категорії') # Зворотнє связування відбувається через posts але якщо його не булоб визначено то треба булоб писати women_set
    tags = models.ManyToManyField('TagPost', blank=True, related_name='tags', verbose_name='Тег')  # related_name тут задається імя менеджер звязування (і до нього можна звертатися)
    husband = models.OneToOneField('Husband', on_delete=models.SET_NULL,
                                   null=True, blank=True, related_name='women', verbose_name='Чоловік')

    objects = models.Manager()  #  який перший той і дефолтний для адмін панелі!!!!!!!!!!!!!!!!!!!!
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Відомі жінки'
        verbose_name_plural = 'Відомі жінки'
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(translit_to_eng(self.title))
        super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='категорія')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Катерогії'
        verbose_name_plural = 'Катерогії'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})


class Husband(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    m_count = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.name
