from rest_framework import serializers
from NormalSerializer.models import Employee


# built-in validation
def multiples_of_1000(value):  # normal fun
    if value % 1000 != 0:
        raise serializers.ValidationError("Salary should be multiples of 1000.")


class EmployeeSerializer(serializers.ModelSerializer):
    esal = serializers.FloatField(validators=[multiples_of_1000])

    class Meta:
        model = Employee
        fields = "__all__"
        # fields = ['eno','ename']  # include only specified fields
        # fields = ('eno','ename')   
        # exclude = ['esal']    # exclude only specified fields
