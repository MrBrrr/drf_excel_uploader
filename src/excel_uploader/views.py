# Create your views here.
from typing import Dict, List

import pandas as pd
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework.request import Request
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from excel_uploader.serializers import ExcelSerializer


class UploaderView(ViewSet):
    """ Introduces POST and GET methods for Excel Serializer. """
    
    serializer_class = ExcelSerializer

    def list(self, request) -> Response:
        """
        POST method.

        :return: http response with simple communication message.
        """
        return Response("Nothing uploaded yet.")

    def create(self, request: Request) -> Response:
        """
        POST method.

        :param request: http request containing uploaded file and chosen columns.
        :return: http response with excel summary.
        """
        file_uploaded = request.FILES.get("upload_file")
        column_names = request.data.get("column_names")
        summary = self._summarize_data_frame(
            data_frame=self._adjust_excel_file(xlsx_file=file_uploaded, headers=column_names))
        response = {"filename": file_uploaded.name, "summary": summary}
        return Response(response)

    @staticmethod
    def _adjust_excel_file(xlsx_file: InMemoryUploadedFile, headers: str) -> pd.DataFrame:
        """
        Cuts out redundant data from .xlsx file and transforms result to pandas data frame.

        :param xlsx_file: bytes representation of uploaded .xlsx file.
        :param headers: columns' headers to be captured in summary.
        :return: data frame of required columns.
        """
        xlsx_file.seek(0)
        content_df = pd.read_excel(xlsx_file.read())
        content_df.columns = content_df.iloc[1]
        return content_df.loc[2:, [column.strip() for column in headers.split(",")]].reset_index(drop=True)

    @staticmethod
    def _summarize_data_frame(data_frame: pd.DataFrame) -> List[Dict]:
        """
        Summarize data - calculates average and sum for each column of data frame.

        :param data_frame: pandas data frame.
        :return: list of dictionaries containing summaries for each column.
        """
        return [dict(zip(("column", "avg", "sum"), row))
                for row in zip(data_frame.columns, data_frame.mean(), data_frame.sum())]
