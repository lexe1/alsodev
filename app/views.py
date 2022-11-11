from django.shortcuts import render, redirect
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Item, Image
from .forms import ItemForm

from .serializers import ItemSerializer


def add(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        images = request.FILES.getlist('images')
        if form.is_valid():
            item = form.save()
            for image in images:
                Image.objects.create(item=item, image=image)
                if len(images) > 1 and str(image) not in item.images:
                    item.images += ', ' + str(image)
            form.save()
            # return redirect('/')
    return render(request, 'add.html', {'form': form})


@ api_view(['GET'])
def List(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@ api_view(['GET'])
def Details(request, pk):
    item = Item.objects.get(id=pk)
    serializer = ItemSerializer(item, many=False)
    return Response(serializer.data)


@ api_view(['POST'])
def Create(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@ api_view(['POST'])
def Update(request, pk):
    item = Item.objects.get(id=pk)
    serializer = ItemSerializer(instance=item, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@ api_view(['DELETE'])
def Delete(request, pk):
    item = Item.objects.get(id=pk)
    item.delete()
    return Response('Item deleted.')
