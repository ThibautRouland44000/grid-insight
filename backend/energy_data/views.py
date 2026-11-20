from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .models import Reading
from .serializers import ReadingSerializer


@api_view(["GET"])
def health(request):
    return Response({"status": "ok"})


class ReadingListView(ListAPIView):
    queryset = Reading.objects.all().order_by("recorded_at", "source")
    serializer_class = ReadingSerializer
