from django.contrib import admin
from forum.models import question, answer

class AnswerInline(admin.TabularInline):
    model = answer

class QuestionsAdmin(admin.ModelAdmin):

    inlines = [AnswerInline]
    class Meta:
        model = question


admin.site.register(question)
admin.site.register(answer)
