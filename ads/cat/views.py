import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from ads.models import Categories


class CatListView(ListView):
    model = Categories

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object_list = self.object_list.order_by('name')
        data = [{'id': cat.pk, 'name': cat.name} for cat in self.object_list]
        return JsonResponse(data, safe=False)


class CatDetailView(DetailView):
    model = Categories

    def get(self, request, *args, **kwargs):
        cat = self.get_object()
        return JsonResponse({
            'id': cat.id,
            'name': cat.name
        })


@method_decorator(csrf_exempt, name='dispatch')
class CatCreateView(CreateView):
    model = Categories
    fields = "__all__"

    def post(self, request, *args, **kwargs):
        new_data = json.loads(request.body)
        add = Categories.objects.create(**new_data)
        return JsonResponse({
            "id": add.id,
            "name": add.name,
        })


@method_decorator(csrf_exempt, name='dispatch')
class CatUpdateView(UpdateView):
    model = Categories
    fields = ["name"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        new_data = json.loads(request.body)
        self.object.name = new_data['name']
        self.object.save()
        return JsonResponse({
            "name": self.object.name
        })


@method_decorator(csrf_exempt, name='dispatch')
class CatDeleteView(DeleteView):
    model = Categories
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({"status": "deleted"}, status=200)
