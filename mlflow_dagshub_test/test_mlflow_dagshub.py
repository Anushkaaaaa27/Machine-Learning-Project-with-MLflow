import mlflow
import os
import logging

# Increase logging level to get more detailed information
logging.basicConfig(level=logging.DEBUG)

# Set DagsHub credentials using token
os.environ['MLFLOW_TRACKING_USERNAME'] = 'Anushkaaaaa27'
os.environ['MLFLOW_TRACKING_PASSWORD'] = 'd765053210f02ed6b784c2e293081bc4cb05e329'

# Set the MLflow tracking URI to DagsHub
mlflow.set_tracking_uri('https://dagshub.com/Anushkaaaaa27/Machine-Learning-Project-with-MLflow.mlflow')

# Start an MLflow run and log parameters and metrics
with mlflow.start_run() as run:
    mlflow.log_param("param1", "value1")
    mlflow.log_metric("metric1", 0.5)
    print(f"Run ID: {run.info.run_id}")
