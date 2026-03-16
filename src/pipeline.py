import pandas as pd
import os

class TaxiPipeline:
    def __init__(self, folder_path="../data/raw"):
        """
        Initializes the pipeline with a default folder path.
        """
        self.folder_path = folder_path
        self.df = None

    def load_data(self, file_name):
        """
        Joins the folder path and file name, then loads the parquet file.
        """
        # 1. Construct the full path
        full_path = os.path.join(self.folder_path, file_name)
        
        print(f" Attempting to load: {full_path}")
        
        # 2. Check if file exists before loading
        if os.path.exists(full_path):
            try:
                self.df = pd.read_parquet(full_path, engine='pyarrow')
                print(" Data loaded successfully!")
                return self.df
            except Exception as e:
                print(f" An error occurred during reading: {e}")
                return None
        else:
            print(f"Error: File not found at {full_path}")
            return None

# --- Execution Block (Only runs if you run this file directly) ---
if __name__ == "__main__":
    # If running from the root, we use 'data/raw'
    RAW_DATA_PATH = "data/raw"
    FILE_NAME = "yellow_tripdata_2024-01.parquet" 
    
    pipeline = TaxiPipeline(RAW_DATA_PATH)
    taxi_df = pipeline.load_data(FILE_NAME)
    
    if taxi_df is not None:
        print(f" Dataset contains {taxi_df.shape[0]} rows and {taxi_df.shape[1]} columns.")