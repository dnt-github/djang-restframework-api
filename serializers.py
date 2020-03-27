from rest_framework import serializers
from .models import Customer, Profession, DataSheet, Document


class DataSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSheet
        fields = ('id', 'description', 'historical_data')


class CustomerSerializer(serializers.ModelSerializer):
    num_professions = serializers.SerializerMethodField()
    #data_sheet = serializers.PrimaryKeyRelatedField(read_only=True)
    #data_sheet = serializers.SerializerMethodField()
    data_sheet = DataSheetSerializer()
    professions = serializers.StringRelatedField(many=True)
    document_set = serializers.StringRelatedField(many=True)

    class Meta:
        model = Customer
        fields = ('id', 'name', 'address', 'professions', 'data_sheet',
                  'active', 'status_sentence', 'num_professions','document_set')

    def get_num_professions(self, obj):
        return obj.num_professions()


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ('id', 'description')




class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'dtype', 'doc_number', 'customer')
