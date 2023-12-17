from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform,Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Review
        exclude=('watchlist',)
        #fields = "__all__"

        
#======================using modelserializer================
class WatchListSerializer(serializers.ModelSerializer):
    ##**len_name=serializers.SerializerMethodField()  #custom serializer fields for finding the length of movie-name/watchlist
    #IT DISABLE REVIEW/RATING
    # reviews = ReviewSerializer(many=True,read_only=True)
    platform = serializers.CharField(source='platform.name')

  
# class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=WatchList
        fields="__all__"
    
#         #fields=['id','name','description'] #for all the fields__all__
#         exclude=['id'] #for excluding the id feild


#==============================================================
    
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True,read_only=True)
    
#=============================for hyperlink==========================
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='movie-detail'
    #     )

    class Meta:
        model=StreamPlatform
        fields="__all__"
        
        
#====================custom fields validators ===========12/12/23
    # def get_len_name(self,object):
    #     return len(object.name)
         
        
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError('name and description should be same!')
    #     else:
    #         return data
    
    # #field level validator
    # def validate_name(self,value):
    #     if len(value)<2:
    #         raise serializers.ValidationError("Name is too short")
    #     else:
    #         return value
        
    
    
# def name_length(self,value):
#     if len(value)<2:
#         raise serializers.ValidationError("Name is too short!")

#=====================================================================
# class MovieSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField() #validators=[name_length]
#     description=serializers.CharField()
#     active=serializers.BooleanField()
    
# #post=======add data from user side
#     def create(self,validated_data):
#       return Movie.objects.create(**validated_data)

# #put====update the data 
#     def update(self,instance,validated_data):
#         instance.name=validated_data.get('name',instance.name)
#         instance.description=validated_data.get('description',instance.description)
#         instance.active=validated_data.get('active',instance.active)
#         instance.save()
#         return instance

# #obj-level validation
#     def validate(self,data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("name and description should be different")
#         else:
#             return data 
            

# #field level validator
#     def validate_name(self,value):
#         if len(value)<2:
#             raise serializers.ValidationError("Name is too short")
#         else:
#             return value

# #delete 
#     def delete(self,validated_data):
#       return Movie.objects.delete(**validated_data)