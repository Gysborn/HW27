import json

from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from HW27_Avito import settings
from ads.models import Categories, Ad
from users.models import User


def index(request):
    return HttpResponse({"status": "ok"}, 200)


class AdListView(ListView):
    model = Ad
    queryset = Ad.objects.all()

    def get(self, request, *args, **kwargs):
        cat = request.GET.get('cat', None)
        text = request.GET.get('text', None)
        price_from = request.GET.get('price_from', None)
        price_to = request.GET.get('price_to', None)
        if cat:
            self.queryset = self.queryset.filter(
                category__id__contains=cat)
            super().get(request, *args, **kwargs)
        if text:
            self.queryset = self.queryset.filter(
                name__icontains=text)
            super().get(request, *args, **kwargs)
        if price_from or price_to:
            if not price_to:
                price_to = 100000
            if not price_from:
                price_from = 0
            self.queryset = self.queryset.filter(
                price__range=(price_from, price_to))
        super().get(request, *args, **kwargs)

        self.object_list = self.object_list.order_by('-price')
        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        data = [{
            "id": ad.id,
            "name": ad.name,
            "author": ad.author.username,
            "price": ad.price,
            "category": ad.category.name,
            "description": ad.description,
            "is_published": ad.is_published,
            "image": ad.image.url if ad.image else None
        } for ad in page_obj]

        return JsonResponse({
            'items': data,
            'num_pages': paginator.num_pages,
            'total': paginator.count
        }, safe=False)


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author.username,
            "price": ad.price,
            "category": ad.category.name,
            "description": ad.description,
            "is_published": ad.is_published,
            "image": ad.image.url if ad.image else None,
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    model = Ad
    fields = ["name", "author_id", "price", "category_id", "description", "is_published"]

    def post(self, request, *args, **kwargs):
        new_data = json.loads(request.body)
        author = get_object_or_404(User, pk=new_data["author"])
        category = get_object_or_404(Categories, pk=new_data["category"])
        result = Ad.objects.create(
            name=new_data["name"],
            author=author,
            price=new_data["price"],
            description=new_data.get("description", ""),
            category=category,
            is_published=new_data.get("is_published", False),
        )
        return JsonResponse({
            "id": result.id,
            "name": result.name,
            "author": result.author.username,
            "price": result.price,
            "category": result.category.name,
            "description": result.description,
            "is_published": result.is_published
        }, safe=False)


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


@method_decorator(csrf_exempt, name='dispatch')
class AdUpdateView(UpdateView):
    model = Ad
    fields = ["name", "author", "price", "category", "description", "is_published"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        up_data = json.loads(request.body)
        keys = up_data.keys()
        if 'author' in keys:
            up_data['author'] = get_object_or_404(User, pk=up_data['author'])
        if 'category' in keys:
            up_data['category'] = get_object_or_404(Categories, pk=up_data["category"])
        [setattr(self.object, k, v) for k, v in up_data.items()]
        self.object.save()
        return JsonResponse({"status": "updated"}, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdDeleteView(DeleteView):
    model = Ad
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({"status": "deleted"}, status=200)
