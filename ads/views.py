import json

from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Categories, Ad


def index(request):
    return HttpResponse({"status": "ok"}, 200)


@method_decorator(csrf_exempt, name='dispatch')
class CatView(View):
    def get(self, request):
        cat = Categories.objects.all()

        result = []
        for row in cat:
            result.append({
                'id': row.id,
                'name': row.name
            })
        return JsonResponse(result, safe=False)

    def post(self, request):
        new_data = json.loads(request.body)
        add = Categories.objects.create(**new_data)
        return JsonResponse({
            "id": add.id,
            "name": add.name,
        })



@method_decorator(csrf_exempt, name='dispatch')
class AdView(View):
    def get(self, request):
        ad = Ad.objects.all()

        result = []
        for row in ad:
            result.append({
                "id": row.id,
                "name": row.name,
                "author": row.author,
                "price": row.price,
                "description": row.description,
                "address": row.address,
                "is_published": row.is_published
            })
        return JsonResponse(result, safe=False)

    def post(self, request):
        new_data = json.loads(request.body)
        add = Ad.objects.create(**new_data)
        return JsonResponse({
                "id": add.id,
                "name": add.name,
                "author": add.author,
                "price": add.price,
                "description": add.description,
                "address": add.address,
                "is_published": add.is_published
        })


class CatDetailView(DetailView):
    model = Categories

    def get(self, request, *args, **kwargs):
        cat = self.get_object()
        return JsonResponse({
            'id': cat.id,
            'name': cat.name
        })


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        return JsonResponse({
                "id": ad.id,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price,
                "description": ad.description,
                "address": ad.address,
                "is_published": ad.is_published
        })