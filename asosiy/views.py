from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, filters
from rest_framework.viewsets import ModelViewSet

from .serializers import *
from .models import *

class QoshiqAPIView(APIView):
    def get(self, request):
        qoshiqlar = Qoshiq.objects.all()
        serializer = QoshiqSerializer(qoshiqlar, many=True)
        return Response(serializer.data)

    def post(self, request):
        qoshiq =request.data
        serializer = QoshiqSerializer(data = qoshiq)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class QoshiqchiAPIView(APIView):
#     def get(self, request):
#         qoshiqlar = Qoshiqchi.objects.all()
#         serializer = QoshiqchiSerializer(qoshiqlar, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         qoshiq =request.data
#         serializer = QoshiqchiSerializer(data = qoshiq)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class AlbomAPIView(APIView):
#     def get(self, request):
#         qoshiqlar = Albom.objects.all()
#         serializer = AlbomSerializer(qoshiqlar, many=True)
#         return Response(serializer.data)

# class QoshiqchiDetailAPIView(APIView):
#     def get(self, request, pk):
#         qoshiqlar = Qoshiqchi.objects.get(id=pk)
#         serializer = QoshiqchiSerializer(qoshiqlar)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         aktyor = Qoshiqchi.objects.get(id=pk)
#         serializer = QoshiqchiSerializer(aktyor, data=request.data)
#         if serializer.is_valid():
#             aktyor.ism = serializer.validated_data.get('ism')
#             aktyor.davlat = serializer.validated_data.get('davlat')
#             aktyor.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class QoshiqchiDeleteAPIView(APIView):
#     def get(self, request, pk):
#         qoshiqchi = Qoshiqchi.objects.get(id=pk)
#         if qoshiqchi:
#             qoshiqchi.delete()
#             return Response(status=status.HTTP_202_ACCEPTED)
#         return Response(status=status.HTTP_204_NO_CONTENT)

class QoshiqchilarViewSet(ModelViewSet):
    queryset = Qoshiqchi.objects.all()
    serializer_class = QoshiqchiSerializer

    def get_queryset(self):
        soz = self.request.query_params.get('qidirish')
        if soz is None or soz == "":
            natija = Qoshiqchi.objects.all()
        else:
            natija = Qoshiqchi.objects.filter(ism__contains=soz)
        return natija

    @action(detail=True, methods=['GET', 'POST', 'PUT'])
    def albomlar(self, request, pk):
        if request.method == 'POST':
            serializer = AlbomSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(qoshiqchi=Qoshiqchi.objects.get(id=pk))
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        if request.method == 'PUT':
            serializer = AlbomSerializer(albom, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        qoshiqchi = Qoshiqchi.objects.get(id=pk)
        albom = Albom.objects.filter(qoshiqchi=qoshiqchi)
        serializer = AlbomSerializer(albom, many=True)
        return Response(serializer.data)

class AlbomViewSet(ModelViewSet):
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer
    filter_backends = [filters.SearchFilter,]
    search_fields = ('nom', 'qoshiqchi__ism')

class QoshiqViewSet(ModelViewSet):
    queryset = Qoshiq.objects.all()
    serializer_class = QoshiqSerializer