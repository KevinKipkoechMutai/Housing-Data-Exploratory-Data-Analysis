import os
import zipfile
import pandas as pd
from abc import ABC, abstractmethod

# Abstract class for data ingestion
class DataIngestor(ABC):
    @abstractmethod
    def ingest_data(self, data_path: str) -> pd.DataFrame:
        pass


class ZipDataIngestor(DataIngestor):
    def ingest_data(self, file_path: str) -> pd.DataFrame:
        #ensure the file is a .zip
        if not file_path.endswith('.zip'):
            raise ValueError('The file must be a .zip file')
        
        #extract the contents of the zip file
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall("extracted_data")

        #find the first csv file in the extracted data
        extracted_files = os.listdir("extracted_data")
        csv_files = [f for f in extracted_files if f.endswith('.csv')]

        if len(csv_files) == 0:
            raise ValueError('No CSV files found in the extracted data')
        
        if len(csv_files) > 1:
            raise ValueError("More than one CSV file found. Specify one.")

        #read the csv file into a pandas dataframe
        csv_file_path = os.path.join("extracted_data", csv_files[0])
        df = pd.read_csv(csv_file_path)

        return df

#implement a factory method to create the appropriate data ingestor
class DataIngestorFactory:
    @staticmethod
    def get_ingestor(file_extension: str) -> DataIngestor:
        if file_extension == '.zip':
            return ZipDataIngestor()
        else:
            raise ValueError(f"Unsupported file extension: {file_extension}")
    

if __name__ == "__main__":
    ingestor = DataIngestorFactory.get_ingestor('.zip')
    df = ingestor.ingest_data('data/archive.zip')
    print(df.head())
