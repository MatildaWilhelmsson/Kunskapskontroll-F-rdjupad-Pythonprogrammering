
import pandas as pd
from API_module import API
from DataCleaner_module import DataCleaner
from ToSQL_module import ToSQL

api = API()
dc = DataCleaner()
sql = ToSQL()

url = "https://skatteverket.entryscape.net/rowstore/dataset/c67b320b-ffee-4876-b073-dd9236cd2a99?%C3%A5r=2024&_limit=500&_offset=0"

data = api.load_data(url)
cleaned_data = dc.data_cleaner(data)
sql.sql_saver(cleaned_data)


def test_load_data():
        # Test to make sure the response status from API returns 200 (download successfull). 
        response = api.load_data(url)
        assert response.status_code == 200


def test_data_cleaner():
        # Test to make sure the data_cleaner returns a pd.DataFrame object.
        assert isinstance(dc.data_cleaner(data), pd.DataFrame)


def test_sql_saver():
        # Test to make sure sql_saver saves a file containing 90 municipalities (the ones accessed by the API).
        assert sql.sql_saver(cleaned_data) == 90