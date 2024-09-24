
import logging
from API_module import API
from DataCleaner_module import DataCleaner
from ToSQL_module import ToSQL


# Initiating a logger object that will track our script while it runs.
logger = logging.getLogger(__name__)

logging.basicConfig(
    filename='main.log', 
    format='[%(asctime)s][%(name)s][%(levelname)s] %(message)s', 
    datefmt='%Y-%m-%d %H:%M:%S', 
    level=logging.INFO)


# Link to the API from where we wanna draw our data. In this case Skatteverket, kommunalskatter.
url = "https://skatteverket.entryscape.net/rowstore/dataset/c67b320b-ffee-4876-b073-dd9236cd2a99?%C3%A5r=2024&_limit=500&_offset=0"

### Faulty url för exception test.
###url = "https://skatteverket.entryscape.net/rowstore/dataset/c67b320b-ffee-4876-b073-dd9236cd2a99?%C3%A5r=2024&_limit=500&_offset=0x"


# Creating instances of the different classes we created in our modules so that they can be use in our main script.
api = API()
dc = DataCleaner()
sql = ToSQL()

logger.info("Starting data pipeline...")

# Our pipeline to load, process and save the data from the API.
data = api.load_data(url)
cleaned_data = dc.data_cleaner(data)
sql.sql_saver(cleaned_data)

logger.info("Pipeline completed. Data accessed, processed and loaded into SQL-table.")