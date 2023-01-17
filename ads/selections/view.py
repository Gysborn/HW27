from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ads.models import Selections
from ads.selections.permissions import IsSelectionOwner
from ads.selections.serializer import SelectionsSerializer, SelectionListSerializer, SelectionDetailSerializer, \
    SelectionsCreateSerializer


class SelectionsViewSet(ModelViewSet):
    queryset = Selections.objects.all()
    default_serializer = SelectionsSerializer

    serializer_classes = {
        "list": SelectionListSerializer,
        "retrieve": SelectionDetailSerializer,
        "create": SelectionsCreateSerializer,
    }

    default_permission = [AllowAny()]
    permissions = {
        "retrieve": [IsAuthenticated()],
        "create": [IsAuthenticated()],
        "delete": [IsAuthenticated(), IsSelectionOwner()],
        "partial_update": [IsAuthenticated(), IsSelectionOwner()],
        "update": [IsAuthenticated(), IsSelectionOwner()],
    }

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission)

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)

