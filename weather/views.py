# Create your views here.
from rest_framework.generics import ListAPIView

from .serializers import WeatherSerializers
from .response_data import get_parsed_data
from .models import Weather
from .predictions import coordinate_prediction


class WeatherListView(ListAPIView):
    # queryset = get_parsed_data()  # Weather.objects.all() #getData()

    queryset = Weather.objects.all()
    serializer_class = WeatherSerializers
    coordinate_prediction()
