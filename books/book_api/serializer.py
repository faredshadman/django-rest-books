# from rest_framework import serializers
# from book_api.models import Book
# class BookSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField()
#     number_of_pages = serializers.IntegerField()
#     publish_date = serializers.DateField()
#     quantity = serializers.IntegerField()
    
#     def create(self,  data):
#         return Book.objects.create(**data)
#     def update(self, instance, data):
#         instance.title = data.get('title',instance.title)
#         instance.number_of_pages = data.get('number_of_pages',instance.number_of_pages)
#         instance.publish_date = data.get('publish_date',instance.publish_date)
#         instance.quantity = data.get('quantity',instance.quantity)
        
#         instance.save()
#         return instance

from rest_framework import serializers
from  book_api.models import Book
from django.forms import ValidationError

class BookSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = '__all__'
    def validate_title(self,value):
        if value == 'abc':
            raise ValidationError('Title cannot be abc')
        return value
    def validate(self,data):
        if data['number_of_pages'] > 1000 and data['quantity'] > 100:
            raise ValidationError('Number of pages cannot be greater than 1000 or quantity cannot be greater than 100')
        return data
    def get_description(self,obj):
        return f'{obj.title} is a good book and has {obj.number_of_pages} pages and was published on {obj.publish_date} and has {obj.quantity} copies'
    
    
   