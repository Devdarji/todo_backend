from rest_framework import serializers


class CardSerializer(serializers.Serializer):
    card_name = serializers.CharField(required=True)
