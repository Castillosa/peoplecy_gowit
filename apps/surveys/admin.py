from django.contrib import admin

# Register your models here.

from .models import Survey, SurveyAnswer, SurveyType, SurveyQuestion


class SurveyQuestionInline(admin.TabularInline):
    model = SurveyQuestion
    extra = 1
    list_display = ('survey', 'question', 'type', 'order', 'is_required')
    show_change_link = True


class SurveyAdmin(admin.ModelAdmin):
    list_display = ('name', 'hash_id', 'is_active', 'is_public', 'is_anonymous')
    list_filter = ('is_active', 'is_public', 'is_anonymous')
    search_fields = ('name', 'description')
    inlines = [SurveyQuestionInline]


class SurveyQuestionAdmin(admin.ModelAdmin):
    list_display = ('survey', 'question_text', 'type', 'order', 'is_required')
    list_filter = ('survey', 'type', 'is_required')
    search_fields = ('survey', 'question')
    filter_horizontal = ['components', 'attributes']


class SurveyAnswerAdmin(admin.ModelAdmin):
    list_display = ('is_anonymous', 'answer_order', 'question', 'value', 'created_at', 'updated_at')


class SurveyTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'is_public')
    list_filter = ('is_active', 'is_public')
    search_fields = ('name', 'description')


admin.site.register(SurveyQuestion, SurveyQuestionAdmin)
admin.site.register(SurveyType, SurveyTypeAdmin)
admin.site.register(SurveyAnswer, SurveyAnswerAdmin)
admin.site.register(Survey, SurveyAdmin)
