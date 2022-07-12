from .models import Wine, Winemaker
from rest_framework import generics
from .serializers import WineSerializer, WinemakerSerializer

# Create your views here.


class WineList(generics.ListCreateAPIView):
    queryset = Wine.objects.all()
    serializer_class = WineSerializer


class WineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wine.objects.all()
    serializer_class = WineSerializer


class WinemakerList(generics.ListCreateAPIView):
    queryset = Winemaker.objects.all()
    serializer_class = WinemakerSerializer


class WinemakerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Winemaker.objects.all()
    serializer_class = WinemakerSerializer