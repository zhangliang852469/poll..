from django.contrib import admin

# Register your models here.

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):

    search_fields = ['question_text']

    list_filter = ['pub_date']

    fieldsets = [
        ('问题', {'fields': ['question_text']}),
        ('创建时间', {'fields': ['pub_date']}),
    ]

    inlines = [ChoiceInline]

    list_display = ('id', 'question_text', 'pub_date')
    ordering = ('-id',)

admin.site.register(Question, QuestionAdmin)

