from abc import ABC, abstractmethod
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#abstract base class for bivariate analysis
class BivariateAnalysisStrategy(ABC):
    @abstractmethod
    def analyze(self, df: pd.DataFrame, feature1: str, feature2: str):
        pass


#numerical vs numerical analysis
class NumericalVsNumericalAnalysis(BivariateAnalysisStrategy):
    def analyze(self, df: pd.DataFrame, feature1: str, feature2: str):
        plt.figure(figsize=(10,6))
        sns.scatterplot(x=feature1, y=feature2, data=df)
        plt.title(f'Scatter Plot of {feature1} vs {feature2}')
        plt.xlabel(feature1)
        plt.ylabel(feature2)
        plt.show()
    
#categorical vs numerical analysis
class CategoricalVsNumericalAnalysis(BivariateAnalysisStrategy):
    def analyze(self, df: pd.DataFrame, feature1: str, feature2: str):
        plt.figure(figsize=(10,6))
        sns.boxplot(x=feature1, y=feature2, data=df)
        plt.title(f'Box Plot of {feature2} by {feature1}')
        plt.xlabel(feature1)
        plt.ylabel(feature2)
        plt.xticks(rotation=45)
        plt.show()

#context class for bivariate analysis
class BivariateAnalyzer:
    def __init__(self, strategy: BivariateAnalysisStrategy):
        self._strategy = strategy
    
    def set_strategy(self, strategy: BivariateAnalysisStrategy):
        self._strategy = strategy
    
    def execute_analysis(self, df: pd.DataFrame, feature1: str, feature2: str):
        self._strategy.analyze(df, feature1, feature2)


if __name__ == "__main__":
    pass

