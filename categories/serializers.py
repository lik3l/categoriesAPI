from rest_framework import serializers

from categories.models import Category


def save_categories(categories, initial_parent=None):
    instances = list()
    for category in categories:
        children = category.pop('children', None)
        parent = Category.objects.create(**category, parent=initial_parent)
        serialized = CategorySerializer(parent).data
        if children:
            serialized['children'] = save_categories(children, parent)
        instances.append(serialized)

    return instances


class SimpleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class CategorySerializer(serializers.ModelSerializer):
    children = serializers.JSONField(required=False, write_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'children')

    def validate_children(self, children):
        serializer = CategorySerializer(data=children, many=True, context=self.context)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data

    def create(self, validated_data):
        children = validated_data.pop('children', None)
        instance = Category.objects.create(**validated_data)
        resp = CategorySerializer(instance).data
        if children:
            resp['children'] = save_categories(children, instance)

        return resp


class RetrieveSerializer(serializers.ModelSerializer):
    parent = SimpleCategorySerializer(read_only=True)
    children = SimpleCategorySerializer(read_only=True, many=True)
    siblings = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'parent', 'children', 'siblings')

    def get_siblings(self, instance):
        return SimpleCategorySerializer(instance.siblings, many=True).data
