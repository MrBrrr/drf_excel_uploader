# Create your views here.
import io

import pandas as pd
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from excel_uploader.serializers import ExcelSerializer


class UploaderView(ViewSet):
    serializer_class = ExcelSerializer

    def list(self, request):
        return Response("list_view")

    def create(self, request, format=None):
        file_uploaded = request.FILES.get("file_uploaded")
        column_names = request.data.get("column_names")
        summary = self._summarize_chosen_columns(excel_bytes=file_uploaded, columns=column_names.split(","))
        response = {"filename": file_uploaded.name, "summary": summary}
        return Response(response)

    def _summarize_chosen_columns(self, excel_bytes, columns):
        content_bytes = io.BytesIO()
        content_bytes.write(excel_bytes)
        content_bytes.seek(0)

        content_pd = pd.DataFrame(content_bytes)

        return self
