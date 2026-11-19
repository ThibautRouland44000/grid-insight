from rest_framework import serializers

from .models import Reading


class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = ["recorded_at", "source", "value_mw"]
