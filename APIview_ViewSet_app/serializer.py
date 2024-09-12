from rest_framework import serializers
from APIview_ViewSet_app.models import Student

# here we not use ModelSerializer because we dont have model. we just use serializer.
class NameSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"