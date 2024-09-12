from rest_framework import serializers
from NormalSerializer.models import Employee

# built-in validation
def multiples_of_1000(value):   # normal fun
    if value % 1000 != 0:
        raise serializers.ValidationError("Salary should be multiples of 1000.")

class EmployeeSerializer(serializers.Serializer):
    eno=serializers.IntegerField()
    ename=serializers.CharField(max_length=64)  # max length is built-in validation
    esal=serializers.FloatField(validators=[multiples_of_1000])
    eaddr=serializers.CharField()

    # field level validator
    def validate_esal(self, value): 
        if value < 5000:
            raise serializers.ValidationError("Employee salary should be minimum 5000.")
        return value
    
    # object/global level validator
    def validate(self, data):   # data contains all data in dict format
        ename = data.get('ename')
        esal = data.get('esal')
        if ename.lower() == 'sunny':
            if esal < 50000:
                raise serializers.ValidationError("Sunny salary should be minimum 50000.")
        return data

    # create object in database then override create method
    def create(self, validated_data):
        return Employee.objects.create(**validated_data)
    
    # update object in databse then override update method. instance is old data, validated_Data is user's provided data(new data)
    def update(self, instance, validated_data):
        instance.eno = validated_data.get('eno', instance.eno)  # update data 
        instance.ename = validated_data.get('ename', instance.ename)    # update data
        instance.esal = validated_data.get('esal', instance.esal)   # update data
        instance.eaddr = validated_data.get('eaddr', instance.eaddr)    # update data
        instance.save() # save instance
        return instance
    

