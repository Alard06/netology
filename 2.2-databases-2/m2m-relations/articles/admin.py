from django.contrib import admin
from django.forms import BaseInlineFormSet, ValidationError

from .models import Article, Scope, Tag

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                count += 1
            if count > 1:
                raise ValidationError('Основным может быть только один раздел')
            else: 
                pass
        if count == 0:
            raise ValidationError('Укажите основной раздел')
        return super().clean()


class ScopeInlines(admin.TabularInline):
    model = Scope
    extra = 2
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInlines,]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass