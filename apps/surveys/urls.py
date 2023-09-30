from django.urls import path

from . import views

app_name = "surveys"
urlpatterns = [
    # path("answer/", views.post_answer, name="post_answer"),
    # path("<str:hash_id>/<str:batch_hash_id>/", views.get_survey, name="survey"),
    # path("<str:batch_hash_id>/", views.get_survey, name="survey_start"),
    # path("<str:batch_hash_id>/<str:sender_type_uid>/<str:sender_uid>/<int:step>", views.get_survey, name="survey_step"),
]
