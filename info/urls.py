from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = "info"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("favicon.ico", views.favicon, name="favicon"),
    path("register/", views.UserCreateView.as_view(), name="register"),
    path("organisations/", views.OrganisationListView.as_view(), name="organisations"),
    path(
        "organisations/<slug:org>/",
        views.OrganisationDetailView.as_view(),
        name="organisation",
    ),
    path(
        "organisations/<slug:org>/volunteer/",
        views.volunteer,
        name="organisation_volunteer",
    ),
    path(
        "organisations/<str:org>/events/",
        views.OrganisationEventListView.as_view(),
        name="organisation_events",
    ),
    path("events/", views.EventListView.as_view(), name="events"),
    path("events/<int:pk>/", views.EventDetailView.as_view(), name="event"),
    path(
        "dashboard/user/<int:pk>/",
        login_required(views.DashboardUserView.as_view()),
        name="dashboard_user",
    ),
    path(
        "dashboard/organisations/",
        login_required(views.DashboardOrganisationView.as_view()),
        name="dashboard_organisations",
    ),
    path(
        "dashboard/organisations/new/",
        login_required(views.DashboardOrganisationCreateView.as_view()),
        name="new_dashboard_organisation",
    ),
    path(
        "dashboard/organisations/<str:org>/",
        login_required(views.DashboardOrganisationUpdateView.as_view()),
        name="dashboard_organisation",
    ),
    path(
        "dashboard/events/",
        login_required(views.DashboardEventListView.as_view()),
        name="dashboard_events",
    ),
    path(
        "dashboard/events/new/",
        login_required(views.DashboardEventCreateView.as_view()),
        name="new_dashboard_event",
    ),
    path(
        "dashboard/events/<int:pk>/",
        login_required(views.DashboardEventUpdateView.as_view()),
        name="dashboard_event",
    ),
    path(
        "dashboard/events/<int:pk>/delete/",
        login_required(views.DashboardEventDeleteView.as_view()),
        name="delete_dashboard_event",
    ),
    path(
        "dashboard/schedule/",
        login_required(views.DashboardiCalScheduleListView.as_view()),
        name="dashboard_schedules",
    ),
    path(
        "dashboard/schedule/new/",
        login_required(views.DashboardiCalScheduleCreateView.as_view()),
        name="new_dashboard_schedule",
    ),
    path(
        "dashboard/schedule/<int:pk>/",
        login_required(views.DashboardiCalScheduleUpdateView.as_view()),
        name="dashboard_schedule",
    ),
    path(
        "dashboard/schedule/<int:pk>/delete/",
        login_required(views.DashboardiCalScheduleDeleteView.as_view()),
        name="delete_dashboard_schedule",
    ),
    path(
        "dashboard/contacts/",
        login_required(views.ContactListView.as_view()),
        name="dashboard_contacts",
    ),
    path(
        "dashboard/contacts/new/",
        login_required(views.ContactCreateView.as_view()),
        name="new_dashboard_contact",
    ),
    path(
        "dashboard/contacts/<int:pk>/",
        login_required(views.ContactUpdateView.as_view()),
        name="dashboard_contact",
    ),
    path(
        "dashboard/contacts/<int:pk>/delete/",
        login_required(views.ContactDeleteView.as_view()),
        name="delete_dashboard_contact",
    ),
    path(
        "dashboard/locations/",
        login_required(views.LocationListView.as_view()),
        name="dashboard_locations",
    ),
    path(
        "dashboard/locations/new/",
        login_required(views.LocationCreateView.as_view()),
        name="new_dashboard_location",
    ),
    path(
        "dashboard/locations/<int:pk>/",
        login_required(views.LocationUpdateView.as_view()),
        name="dashboard_location",
    ),
    path(
        "dashboard/locations/<int:pk>/delete/",
        login_required(views.LocationDeleteView.as_view()),
        name="delete_dashboard_location",
    ),
]
