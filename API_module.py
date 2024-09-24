
import logging
import requests


class API:
    """A class that loads data through an API. 
    Returns the data as a response object."""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
    def load_data(self, url):
        self.logger.info("Connecting to API and downloading data...")
        response = requests.get(url) 
        if not response.status_code == 200:
            self.logger.error("Faulty url. Cannot download data from API.")
            raise Exception("Faulty url. Cannot download data from API.")
        else:
            self.logger.info("API download completed.")
            return response
                