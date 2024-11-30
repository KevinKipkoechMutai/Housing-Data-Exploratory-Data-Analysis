from abc import ABC, abstractmethod
import pandas as pd

#inspection strategy interface
class DataInspectionStrategy(ABC):
    @abstractmethod
    def inspect_data(self, df: pd.DataFrame):
        pass

#data types inspection strategy
class DataTypesInspectionStrategy(DataInspectionStrategy):
    def inspect_data(self, df: pd.DataFrame):
        print("\nData types and Non-null counts:")
        print(df.info())

#summary statistics inspection strategy
class SummaryStatisticsInspectionStrategy(DataInspectionStrategy):
    def inspect_data(self, df: pd.DataFrame):
        print("\n Summary Statistics (Numerical Features):")
        print(df.describe())
        print("\n Summary Statistics (Categorical Features):")
        print(df.describe(include=['O']))


#context class
class DataInspector:
    def __init__(self, strategy: DataInspectionStrategy):
        self._strategy = strategy
    
    def set_strategy(self, strategy: DataInspectionStrategy):
        self._strategy = strategy
    
    def execute_inspection(self, df: pd.DataFrame):
        self._strategy.inspect_data(df)


if __name__ == "__main__":
    pass

