# Create your views here.
import pandas as pd
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from excel_uploader.serializers import ExcelSerializer


class UploaderView(ViewSet):
    serializer_class = ExcelSerializer

    def list(self, request):
        return Response("Nothing uploaded yet.")

    def create(self, request, format=None):
        file_uploaded = request.FILES.get("upload_file")
        column_names = request.data.get("column_names")
        summary = self._summarize_chosen_columns(excel_file=file_uploaded, columns=column_names.split(","))
        response = {"filename": file_uploaded.name, "summary": summary}
        return Response(response)

    def _summarize_chosen_columns(self, excel_file, columns):
        excel_file.seek(0)
        content_df = pd.read_excel(excel_file.read())
        content_df.columns = content_df.iloc[1]
        content_df = content_df[2:].reset_index(drop=True)

        return [
            {"column": column, "avg": content_df[column].mean(), "sum": content_df[column].sum()}
            for column in columns
        ]
