from abc import ABC, abstractmethod
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#abstract base class for multivariate analysis
class MultiVariateAnalysisTemplate(ABC):
    def analyze(self, df: pd.DataFrame):
        self.generate_correlation_matrix(df)
        self.generate_pairplot(df)
    
    @abstractmethod
    def generate_correlation_heatmap(self, df: pd.DataFrame):
        pass

    @abstractmethod
    def generate_pairplot(self, df: pd.DataFrame):
        pass

#multivariate analysis strategy with correlation matrix and pairplot
class SimpleMultiVariateAnalysis(MultiVariateAnalysisTemplate):
    def generate_correlation_heatmap(self, df: pd.DataFrame):
        plt.figure(figsize=(12, 10))
        sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
        plt.title("Correlation Heatmap")
        plt.show()
    
    def generate_pairplot(self, df: pd.DataFrame):
        sns.pairplot(df)
        plt.suptitle("Pairplot of Selected Features", y=1.02)
        plt.show()


if __name__ == "__main__":
    pass

