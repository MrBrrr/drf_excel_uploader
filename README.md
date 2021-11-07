# Excel uploader
___________________________
Upload _.xlsx_ file and calculate summary (average and sum of values) for columns of choice.

___________________________
### Requirements

To fully enjoy this application install all the requirements from: __src\requirements.txt__.

___________________________
### Using the application with _HTML Form_

1. Open the terminal and run the command: 
```shell 
python manage.py runserver
```
2. Copy-paste the link `http://127.0.0.1:8000` to the web browser and navigate to __upload__ section:
`http://127.0.0.1:8000/upload/`.
3. Choose the: __HTML Form__.
4. Complete __Column names__ field with headers that are going to be summarized separated by commas and 
__Choose__ the _.xlsx_ file.

#### Enjoy!

___________________________
### Example:
Uploading the excel file from:   <br>
with column names: `THIS IS THE  PRICE NEW PRICE IN US DOLLARS`
will evaluate:
```doctest
{
    "filename": "us trade price changes2011_nofc.xlsx",
    "summary": [
        {
            "column": "THIS IS THE  PRICE NEW PRICE IN US DOLLARS",
            "avg": 57.07384943631512,
            "sum": 38410.70067064008
        }
    ]
}
```
