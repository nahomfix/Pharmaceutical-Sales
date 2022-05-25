import dvc.api
import mlflow
import pandas as pd

path = "data/train.csv"
repo = "https://github.com/nahomfix/Pharmaceutical-Sales.git"
version = "v1.0"

data_url = dvc.api.get_url(path=path, repo=repo)


mlflow.set_experiment("Rossmann Sales Prediction")


if __name__ == "__main___":

    data = pd.read_csv(data_url, sep=",")

    mlflow.log_param("data_url", data_url)
    mlflow.log_param("data_version", version)

    mlflow.log_artifact("data/train.csv")
    mlflow.log_artifact("data/test.csv")
