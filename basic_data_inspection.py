# from abc import ABC, abstractclassmethod
# import pandas as pd

# class DataInspectionStrategy(ABC):
#     @abstractmethod
#     def inspect(self, df: pd.DataFrame):
#         """
#         Perform a specific type of data inspection.

#         Parameters:
#         df (pd.DataFrame): The dataframe on which the inspection is performed.

#         Returns:
#         None: This method prints the inspection results directly
#         """
#         pass
    
    
# class DataTypesInspectionStrategy(DataInspectionStrategy):
#     def inspect(self, df: pd.DataFrame):
#         print("\nData Types and Non-null Counts:")
#         print(df.info())

        
# class SummaryStatisticsInspectionStrategy(DataInspectionStrategy):
#     def inspect(self, df: pd.DataFrame):
#         print("\nSummary statistics (numerical features):")
#         print(df.describe())
#         print("\nSummary Statistics (Categorical features): ")
#         print(df.describe(include=["0"]))
        
        
# class DataInspector:
#     def __init__(self, strategy: DataInspectionStrategy):
#         self._strategy = strategy
        
#     def set_strategy(self, strategy: DataInspectionStrategy):
#         self._strategy  = strategy
        
#     def execute_inspection(self,df:pd.DataFrame):
#         self._strategy.inspect(df)
        
        
        
        
            

from abc import ABC, abstractmethod
import pandas as pd

class DataInspectionStrategy(ABC):
    @abstractmethod
    def inspect(self, df: pd.DataFrame):
        """
        Perform a specific type of data inspection.

        Parameters:
        df (pd.DataFrame): The dataframe on which the inspection is performed.

        Returns:
        None: This method prints the inspection results directly.
        """
        pass
    
    
class DataTypesInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        print("\nData Types and Non-null Counts:")
        print(df.info())

        
class SummaryStatisticsInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        print("\nSummary statistics (numerical features):")
        print(df.describe())
        print("\nSummary Statistics (Categorical features): ")
        print(df.describe(include=["O"]))
        
        
class DataInspector:
    def __init__(self, strategy: DataInspectionStrategy):
        self._strategy = strategy
        
    def set_strategy(self, strategy: DataInspectionStrategy):
        self._strategy  = strategy
        
    def execute_inspection(self, df: pd.DataFrame):
        self._strategy.inspect(df)
