import os
import zipfile
from abc import ABC, abstractmethod
import pandas as pd

# DEfine abstract class for Data Ingestor

class DataIngestor(ABC):
    @abstractmethod
    def ingest(self, file_path: str) -> pd.DataFrame:
        # abstract method to ingest data from a given file
        pass
    
# implement a concreate class for zip ingestion

class ZipDataIngestor(DataIngestor):
    def ingest(self, file_path: str) -> pd.DataFrame:
        # Ensure the file is a zip
        if not file_path.endswith(".zip"):
            raise ValueError("The file is not a .zip file")

        # Extract the zip file to a directory named "extracted_data"
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall("extracted_data")

        # Find the extracted CSV file
        extracted_files = os.listdir("extracted_data")
        csv_files = [f for f in extracted_files if f.endswith(".csv")]
        
        if len(csv_files) == 0:
            raise FileNotFoundError("No CSV file found")
        elif len(csv_files) > 1:
            print("Multiple CSV files found:")
            for i, file in enumerate(csv_files):
                print(f"{i}: {file}")
            file_index = int(input("Select the file index to process: "))
            csv_file_path = os.path.join("extracted_data", csv_files[file_index])
        else:
            csv_file_path = os.path.join("extracted_data", csv_files[0])

        # Read the selected CSV file into a DataFrame
        df = pd.read_csv(csv_file_path)

        return df


    
# implement a factory to create dataIngestors

class DataIngestorFactory:
    @staticmethod
    def get_data_ingestor(file_extension:str) -> DataIngestor:
        ## returns the appropraiate DataIngestor based on file extension
        if file_extension == ".zip":
            return ZipDataIngestor()
        else:
            raise ValueError({"No ingestor available for file extension: {file_extension}"})
        
        
if __name__ == "__main__":
    
    # specify the path
    #file_path = 'D:\house-price-prediction\data'
    file_path = 'D:\\house-price-prediction\\data\\archive.zip'

    
    # determine the file extension
    file_extension = os.path.splitext(file_path)[1]
    
    # get the appropriate dataIngestor
    data_ingestor = DataIngestorFactory.get_data_ingestor(file_extension)
    
    # ingest the data and load it into a data frame
    
    df = data_ingestor.ingest(file_path)
    
    # now df contains dataframe from the extracted csv
    print(df.head())
    
    
    pass
    
        