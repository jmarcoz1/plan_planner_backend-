from rest_framework import serializers
from .models import Category, Activity, TimeOfDay

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class ActivitySerializer(serializers.ModelSerializer):
    time_of_day = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=TimeOfDay.objects.all()
    )
    category = CategorySerializer()

    class Meta:
        model = Activity
        fields = ['name', 'url', 'category', 'time_of_day']

    def create(self, validated_data):
        time_of_day_data = validated_data.pop('time_of_day')
        category_data = validated_data.pop('category')
        category, _ = Category.objects.get_or_create(name=category_data['name'])
        activity = Activity.objects.create(category=category, **validated_data)
        time_of_day_set = [TimeOfDay.objects.get_or_create(name=name)[0] for name in time_of_day_data]
        activity.time_of_day.set(time_of_day_set)
        return activity

