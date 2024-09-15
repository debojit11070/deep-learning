from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

class MissingValuesAnalysisTemplate(ABC):
    def analyze(self, df:pd.DataFrame):
        
        
        self.identify_missing_values(df)
        self.visualize_missing_values(df)
        
    @abstractmethod
    def identify_missing_values(self, df:pd.DataFrame):
        pass
    
    @abstractmethod
    def visualize_missing_values(self, df:pd.DataFrame):
        pass
    
    
    
class SimpleMissingValuesAnalysis(MissingValuesAnalysisTemplate):
    def identify_missing_values(self, df:pd.DataFrame):
        print("\n missing values count by columns: ")
        missing_values = df.isnull().sum()
        print(missing_values[missing_values>0])
        
    
    def visualize_missing_values(self, df: pd.DataFrame):
        print("\nVisualize Missing Values: ")
        plt.figure(figsize=(12,8))
        sns.heatmap(df.isnull(), cbar = False, cmap= "viridis")
        plt.title("Miissing Values Heatmap")
        plt.show()

    
    
    