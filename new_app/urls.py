from django.urls import path

from new_app.views import IndexView, IndexRedirectView, VacancyCreateView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("article/", IndexRedirectView.as_view(), name="articles_index_redirect"),
    path("article/vacancy/create", VacancyCreateView.as_view(), name="vacancy_create"),
]
