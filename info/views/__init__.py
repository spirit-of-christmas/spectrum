from .contacts import ContactListView, ContactCreateView, ContactDeleteView, ContactDetailView, ContactUpdateView
from .dashboard import DashboardView, dashboard_org
from .events import EventCreateView, EventDeleteView, EventDetailView, EventListview, EventUpdateView, events
from .index import IndexView
from .locations import LocationCreateView, LocationDeleteView, LocationDetailView, LocationListView, LocationUpdateView
from .organisations import (
    organisation,
    organisations,
    organisation_event,
    organisation_events,
    organisation_resource,
    organisation_resources,
)
from .resources import (
    resources,
    ResourceCreateView,
    ResourceDeleteView,
    ResourceDetailView,
    ResourceListview,
    ResourceUpdateView,
)
