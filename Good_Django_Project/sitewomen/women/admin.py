from django.contrib import admin, messages
from .models import Women, Category
from django.utils.safestring import mark_safe


class MarriedFilter(admin.SimpleListFilter):
    title = 'Статус жінок'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'Замужня'),
            ('single', 'Не замужня')
        ]

    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        elif self.value() == 'single':
            return queryset.filter(husband__isnull=True)


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'content', 'photo', 'post_photo', 'cat', 'tags']
    # exclude = ['tags', 'is_published']
    readonly_fields = ['slug', 'post_photo']
    # prepopulated_fields = {'slug': ('title', )} # автозаповнення
    filter_horizontal = ['tags']
    list_display = ('title', 'post_photo', 'time_create', 'is_published', 'cat')
    list_display_links = ('title',)  # клікабельні поля
    ordering = ['-time_create', 'title']
    list_editable = ('is_published',)
    list_per_page = 5
    actions = ['set_published', 'set_draff']
    search_fields = ['title__startswith', 'cat__name']  # тут прикол такий що на cat я неможу послатися бо це форенгкей
                                            # а у звязаних полів можна через __ викликати або люкапи або назви полів таблиці звязаної
    list_filter = [MarriedFilter, 'cat__name', 'is_published']
    save_on_top = True

    # @admin.display(description='Короткий опис', ordering='content')
    # def brief_info(self, women: Women):
    #     return f"Опис {len(women.content)} символів."

    @admin.display(description='Фото', ordering='content')
    def post_photo(self, women: Women):
        if women.photo:
            return mark_safe(f"<img src='{women.photo.url}' width=50")
        return 'Без фото'

    @admin.action(description='Опублікувати вибрані записи')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request, f'Змінено {count} записів')

    @admin.action(description='Зниято з публікації вибрані записи')
    def set_draff(self, request, queryset):
        count = queryset.update(is_published=Women.Status.DRAFT)
        self.message_user(request, f'Змінено {count} записів', messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
