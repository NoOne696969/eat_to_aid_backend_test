from rest_framework import serializers
from .models import CoupounModel,ShopModel

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopModel
        fields =['id','name','lattitude','longitude','address','menu']

class CoupounSerializer(serializers.ModelSerializer):
    #post
    class CoupounCreateSerializer(serializers.ModelSerializer):
        class Meta:
            model = CoupounModel
            fields = ['id', 'name', 'shop', 'discount']
    #get
    shop= ShopSerializer()
    class Meta:
        model = CoupounModel
        fields =['id','name','shop','discount']

