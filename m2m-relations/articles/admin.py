from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Relationship


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
           if form.cleaned_data.get('is_main'):
               counter += 1

        if counter != 1:
            raise ValidationError('У каждой статьи должен быть один  и только один главный тэг')

        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Relationship
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (RelationshipInline,)


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    inlines = (RelationshipInline,)
    exclude = ('articles',)




