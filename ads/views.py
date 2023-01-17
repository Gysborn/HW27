
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ads.models import Ad
from ads.permissions import IsAdOwnerOrStaff
from ads.serializer import AdSerializer, AdDetailSerializer


def index(request):
    return HttpResponse({"status": "ok"}, 200)


class AdViewSet(ModelViewSet):
    queryset = Ad.objects.order_by('-price')
    default_serializer = AdSerializer
    serializer_classes = {
        'list': AdSerializer,
        'retrieve': AdDetailSerializer,
    }
    default_permissions = [AllowAny()]
    permissions = {
        'retrieve': [IsAuthenticated()],
        'update': [IsAuthenticated(), IsAdOwnerOrStaff()],
        'partial_update': [IsAuthenticated(), IsAdOwnerOrStaff()],
        'delete': [IsAuthenticated(), IsAdOwnerOrStaff()],
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permissions)


@method_decorator(csrf_exempt, name='dispatch')
class AdUploadImage(UpdateView):
    model = Ad
    fields = "__all__"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.image = request.FILES.get('image')
        self.object.save()
        return JsonResponse({
            "id": self.object.pk,
            "name": self.object.name,
            "image": self.object.image.url
        })
