from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_ingestion import DataIngestion
from mlProject import logger
import os
from pathlib import Path

STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # Construct the absolute paths for the configuration files
        base_dir = Path(__file__).resolve().parent.parent.parent
        config_dir = base_dir / 'config'
        
        config_filepath = config_dir / 'config.yaml'
        params_filepath = config_dir / 'params.yaml'
        schema_filepath = config_dir / 'schema.yaml'
        
        config = ConfigurationManager(
            config_filepath=config_filepath,
            params_filepath=params_filepath,
            schema_filepath=schema_filepath
        )
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
