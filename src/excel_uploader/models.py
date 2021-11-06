from django.db import models

# Create your models here.


class ExcelUploader(models.Model):
    column_names = models.CharField(max_length=500, default='')
    upload_file = models.FileField()

    def __str__(self):
        return self.upload_file.storage
