
import logging
import pandas as pd

class DataCleaner:
    """A class that loads a response/data object and transforms it into a DataFrame object. 
    The further selects,transforms and sorts the data in the DataFrame according to our specific need."""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
    def data_cleaner(self, response):
        self.logger.info("Turning data into DataFrame...")
        data = response.json() 
        try:
            df = pd.DataFrame(data["results"])
            # df = pd.DataFrame(data["resuts"]) # Faulty DataFrame triggers exception below.
        except:
            self.logger.error("Could not turn data into a pandas DataFrame object.")
            raise Exception ("Could not turn data into a pandas DataFrame object.")
        else:
            self.logger.info("DataFrame-object available.")
            self.logger.info("Processing DataFrame. Selecting, formatting and sorting columns...")
            df = df[["kommun", "summa, exkl. kyrkoavgift"]]
            try:
                df = df.astype({"kommun": "str", "summa, exkl. kyrkoavgift": "float"})
                # df = df.astype({"kommun": "float", "summa, exkl. kyrkoavgift": "float"}) # triggers exception below, "kommun" cannot become a float.
            except:
                self.logger.error("The column-type could not be correctly formatted.")
                raise Exception ("The column-type could not be correctly formatted.")
            else:
                df = df.groupby(by="kommun", as_index=False)["summa, exkl. kyrkoavgift"].mean()
                df = df.sort_values(by="summa, exkl. kyrkoavgift", ascending=False)
                self.logger.info("Processing DataFrame completed.")
        return df 

