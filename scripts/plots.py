import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class Plots:
    def compare_distribution(
        self, dataframe: pd.DataFrame, column: str
    ) -> None:
        sns.displot(dataframe, x=column, binwidth=3)
