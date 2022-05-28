import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler


class DataCleaner:
    def __init__(self, dataframe: pd.DataFrame) -> None:
        self.dataframe = dataframe

    def show_missing_percentages(self) -> pd.Series:
        rows = self.dataframe.shape[0]
        return (self.dataframe.count() / rows) * 100

    def show_missing_counts(self) -> pd.Series:
        return self.dataframe.isnull().sum()

    def convert_to_numeric(self, column: str) -> None:
        self.dataframe[column] = pd.to_numeric(self.dataframe[column])

    def fill_missing_median(self) -> None:
        impute_median = SimpleImputer(strategy="median", missing_values=np.nan)
        numeric_columns = self.dataframe.select_dtypes(include="number")
        self.dataframe = pd.DataFrame(
            impute_median.fit_transform(numeric_columns),
            columns=numeric_columns.columns,
        )

    def scale_dataframe(self) -> None:
        scaler = StandardScaler()
        numeric_columns = self.dataframe.select_dtypes(include="number")
        self.dataframe = pd.DataFrame(
            scaler.fit_transform(numeric_columns),
            columns=numeric_columns.columns,
        )

    def remove_outliers(self, column: str) -> None:
        q3 = self.dataframe[column].quantile(0.75)
        q1 = self.dataframe[column].quantile(0.25)
        iqr = q3 - q1

        upper_outlier = q3 + (1.5 * iqr)
        lower_outlier = q1 - (1.5 * iqr)

        self.dataframe = self.dataframe.loc[
            (self.dataframe[column] > lower_outlier)
            & (self.dataframe[column] < upper_outlier)
        ]

    def remove_closed_stores(self) -> None:
        self.dataframe = self.dataframe.loc[
            (self.dataframe["Open"] != 0) & (self.dataframe["Sales"] != 0)
        ]
