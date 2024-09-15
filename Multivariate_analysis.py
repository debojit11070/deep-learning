from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

class MultiVariateanalysisTemplete(ABC):
    def analyze(self, df:pd.DataFrame):
        self.generate_correlation_heatmap(df)
        self.generate_pairplot(df)
        
    @abstractmethod
    def generate_correlation_heatmap(self, df:pd.DataFrame):
        pass
    
    @abstractmethod
    def generate_pairplot(self, df: pd.DataFrame):
        pass
    
class SimpleMultivariateAnalysis(MultiVariateanalysisTemplete):
    def generate_correlation_heatmap(self, df: pd.DataFrame):
        plt.figure(figsize=(12,10))
        sns.heatmap(df.corr(), annot= True, fmt=".2f", cmap="cool")
        plt.title("correlation Heatmap")
        plt.show()
        
    def generate_pairplot(self, df: pd.DataFrame):
        sns.pairplot(df)
        plt.suptitle("pair plot of selected features", y = 1.02)
        plt.show()
        
    
    