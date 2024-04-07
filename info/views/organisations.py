from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.text import slugify
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from spectrum.settings.base import DEFAULT_FROM_EMAIL
from .. import models


class DashboardOrganisationView(ListView):
    template_name = "info/dashboard.html"
    model = models.Organisation
    paginate_by = 100
    context_object_name = "orgs"

    def get_queryset(self, **kwargs):
        return models.Organisation.objects.filter(
            admin=self.request.user, active=True
        ).order_by("organisation_name")


class DashboardOrganisationCreateView(CreateView):
    model = models.Organisation
    fields = [
        "organisation_name",
        "region",
        "email",
        "website",
        "phone_number",
        "description",
    ]

    def get_success_url(self) -> str:
        return reverse_lazy("info:dashboard_organisations")

    def form_valid(self, form):
        form.instance.admin = self.request.user
        form.instance.active = False
        form.instance.slug = slugify(form.instance.organisation_name)

        return super().form_valid(form)

    def post(self, request):
        post = super().post(request)
        url = request.build_absolute_uri(reverse_lazy("admin:info_organisation_change", args=[self.object.pk]))

        send_mail(
            "Pending Organisation",
            f"'{self.request.user}' has requested to create the organisation '{self.object.slug}', check it out {url}",
            DEFAULT_FROM_EMAIL,
            [DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )

        return post


class OrganisationListView(ListView):
    model = models.Organisation
    paginate_by = 100

    def get_queryset(self, **kwargs):
        return models.Organisation.objects.filter(active=True).order_by(
            "organisation_name"
        )


class OrganisationDetailView(DetailView):
    model = models.Organisation
    slug_field = "slug"
    slug_url_kwarg = "org"
