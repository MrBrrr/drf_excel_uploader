from django.test import TestCase

# Create your tests here.
from src import settings

from excel_uploader.models import ExcelUploader


class TestExcelUploader(TestCase):
    def setUp(self) -> None:
        ExcelUploader.objects.create(column_names="abc, def, ghi", upload_file="ABC.xlsx")
        ExcelUploader.objects.create(column_names="123, 456, 789", upload_file="123.xlsx")

    def test_excel__str__(self):
        letters = ExcelUploader.objects.get(upload_file="ABC.xlsx")
        numbers = ExcelUploader.objects.get(upload_file="123.xlsx")
        self.assertEqual(repr(letters), "<ExcelUploader: ABC.xlsx>")
        self.assertEqual(repr(numbers), "<ExcelUploader: 123.xlsx>")
