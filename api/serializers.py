from rest_framework import serializers
from items.models import Item, FavoriteItem
from django.contrib.auth.models import User



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password',]
    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username,)
        new_user.set_password(password)
        new_user.save()
        return validated_data




class ItemDetailSerializer(serializers.ModelSerializer):
    favourited_by = serializers.SerializerMethodField()
    class Meta:
        model = Item
        fields = ['image', 'name', 'description','favourited_by']

    def get_favourited_by(self,obj):
        favorite = FavoriteItem.objects.filter(user=obj.added_by)
        return favorite
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =  User
        fields = ['first_name', 'last_name',]

class ItemListSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name = "api-detail",
        lookup_field =  "id",
        lookup_url_kwarg = "item_id"
        )
    added_by = UserSerializer()
    favourited = serializers.SerializerMethodField()
    class Meta:
        model = Item
        fields = ['image', 'name', 'description', 'detail','added_by','favourited']
    def get_favourited(self,obj):
        return FavoriteItem.objects.filter(user=obj.added_by).count()
