from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import RedirectView, ListView, CreateView

from accounts.forms import VacancyForm
from new_app.models import Vacancy


class IndexView(ListView):
    template_name = "index.html"
    model = Vacancy
    context_object_name = "vacancies"


class IndexRedirectView(RedirectView):
    pattern_name = "index"


class VacancyCreateView(LoginRequiredMixin, CreateView):
    template_name = "vacancy_create.html"
    model = Vacancy
    form_class = VacancyForm
    success_url = "/"

    def get_success_url(self):
        return reverse_lazy("index")

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = self.request.user
            form.save()
            print(form)
            return redirect(self.success_url)
        context = {"form": form}
        return self.render_to_response(context)
