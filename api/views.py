from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import routers, serializers, viewsets
from api.serializers import GeeksSerializer
from api.models import Geeks
from rest_framework.decorators import api_view


# Create your views here.

# ViewSets define the view behavior.
#class GeeksViewSet(viewsets.ModelViewSet):

@api_view(['GET', 'POST', 'DELETE'])
def geek_list(request):
    if request.method == 'GET':
        geeks = Geeks.objects.all()

        full_name = request.query_params.get('full_name', None)
        if full_name is not None:
            geeks = Geeks.filter(full_name__icontains=full_name)

        geeks_serializer = GeeksSerializer(geeks, many=True)
        return JsonResponse(geeks_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        geeks_data = JSONParser().parse(request)
        geeks_serializer = GeeksSerializer(data=geeks_data)
        if geeks_serializer.is_valid():
            geeks_serializer.save()
            return JsonResponse(geeks_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(geeks_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Geeks.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    try:
        geek = Geeks.objects.get(pk=pk)
    except Geeks.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        geeks_serializer = GeeksSerializer(geek)
        return JsonResponse(geeks_serializer.data)

    elif request.method == 'PUT':
        tutorial_data = JSONParser().parse(request)
        geeks_serializer = GeeksSerializer(geek, data=tutorial_data)
        if geeks_serializer.is_valid():
            geeks_serializer.save()
            return JsonResponse(geeks_serializer.data)
        return JsonResponse(geeks_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        geek.delete()
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)