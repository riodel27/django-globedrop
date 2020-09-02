from accounts.api.views import UserViewSet
from organizations.api.views import OrganizationViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('organizations', OrganizationViewSet)
router.register('users', UserViewSet)
