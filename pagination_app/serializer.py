from rest_framework import serializers
from pagination_app.models import Vendor

class VensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = "__all__"