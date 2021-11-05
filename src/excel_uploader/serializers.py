from rest_framework import serializers

from excel_uploader.models import ExcelUploader


class ExcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExcelUploader
        fields = ["id", "column_names", "file_uploaded"]
