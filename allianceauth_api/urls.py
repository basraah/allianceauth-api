from __future__ import unicode_literals
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from allianceauth_api.views import base, eveonline, optimer, timerboard, srp, groupmanagement, fleetactivitytracking, \
    hrapplications
from rest_framework_swagger.views import get_swagger_view
from . import __version__

schema_view = get_swagger_view(title='AllianceAuth API v'+__version__)

# Create a router and register our viewsets with it.
router = DefaultRouter()

# Base
router.register(r'users', base.UserViewSet)
router.register(r'groups', base.GroupViewSet)
router.register(r'permissions', base.PermissionViewSet)

# Eve
router.register(r'eve/alliances', eveonline.EveAllianceInfoViewSet)
router.register(r'eve/corporations', eveonline.EveCorporationInfoViewSet)
router.register(r'eve/characters', eveonline.EveCharacterViewSet)
router.register(r'eve/api_keys', eveonline.EveApiKeyPairViewSet)

# Optimer
router.register(r'optimers', optimer.OpTimerViewSet)

# Timerboard
router.register(r'timerboard', timerboard.TimerViewSet)

# SRP
router.register(r'srp/fleets', srp.SrpFleetMainViewSet)
router.register(r'srp/requests', srp.SrpUserRequestsViewSet)

# Group Management
router.register(r'groupmanagement/requests', groupmanagement.GroupRequestViewSet)
router.register(r'groupmanagement/authgroups', groupmanagement.AuthGroupViewSet)

# Fleet Activity Tracking
router.register(r'fleetactivitytracking/fats', fleetactivitytracking.FatViewSet)
router.register(r'fleetactivitytracking/fatlinks', fleetactivitytracking.FatlinkViewSet)

# HR Applications
router.register(r'hrapplications/questions', hrapplications.ApplicationQuestionViewSet)
router.register(r'hrapplications/forms', hrapplications.ApplicationFormViewSet)
router.register(r'hrapplications/applications', hrapplications.ApplicationViewSet)
router.register(r'hrapplications/responses', hrapplications.ApplicationResponseViewSet)
router.register(r'hrapplications/comments', hrapplications.ApplicationCommentViewSet)


urlpatterns = [
    url(r'^$', schema_view),
]
urlpatterns += router.urls
