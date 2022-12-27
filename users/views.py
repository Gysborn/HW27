import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from HW27_Avito import settings
from users.models import *


class UserListView(ListView):
    model = User

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        self.object_list = self.object_list.order_by('username')

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        data = [{
            "id": us.id,
            "first_name": us.first_name,
            "last_name": us.last_name,
            "username": us.username,
            "role": us.role,
            "age": us.age,
            "address": [(loc.name, loc.lat, loc.lng) for loc in us.locations.all()],
            "total_ads": us.ad_set.filter(is_published=True).count(),
        } for us in page_obj]

        return JsonResponse({
            'items': data,
            'num_pages': paginator.num_pages,
            'total': paginator.count
        }, safe=False)


class UserDetailView(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        us = self.get_object()
        return JsonResponse({
            "id": us.id,
            "first_name": us.first_name,
            "last_name": us.last_name,
            "username": us.username,
            "role": us.role,
            "age": us.age,
            "address": [(loc.name, loc.lat, loc.lng) for loc in us.locations.all()],
            "total_ads": us.ad_set.filter(is_published=True).count(),
        })


@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(CreateView):
    model = User
    fields = "__all__"

    def post(self, request, *args, **kwargs):
        new_data = json.loads(request.body)
        new_user = User.objects.create(
            first_name=new_data["first_name"],
            last_name=new_data["last_name"],
            username=new_data["username"],
            password=new_data["password"],
            role=new_data["role"],
            age=new_data["age"],
            )

        for loc in new_data.get('locations'):
            location, _ = Location.objects.get_or_create(name=loc)
            new_user.locations.add(location)
        result = {
            "id": new_user.id,
            "first_name": new_user.first_name,
            "last_name": new_user.last_name,
            "username": new_user.username,
            "role": new_user.role,
            "age": new_user.age,
            "locations": [loc.name for loc in new_user.locations.all()]
        }
        return JsonResponse(result, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ["username", "last_name", "first_name", "password", "role", "age", "locations"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        up_data = json.loads(request.body)
        if 'locations' in up_data:
            self.object.locations.all().delete()
            for loc in up_data.get('locations'):
                location, _ = Location.objects.get_or_create(name=loc)
                self.object.locations.add(location)
            del up_data['locations']

        [setattr(self.object, k, v) for k, v in up_data.items()]
        self.object.save()
        return JsonResponse({"status": "updated"}, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({"status": "deleted"}, status=200)