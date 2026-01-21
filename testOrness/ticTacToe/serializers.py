from rest_framework import serializers
from .models import Cell


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cell
        fields = '__all__'

    def validate_x_postion(self, value):
        if value < 0 or value > 2:
            raise serializers.ValidationError('position has to be between 0 and 2.')
        return value

    def validate_y_postion(self, value):
        if value < 0 or value > 2:
            raise serializers.ValidationError('position has to be between 0 and 2.')
        return value