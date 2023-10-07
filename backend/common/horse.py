import pandas as pd

class Horse:
  # コンストラクタ
  def __init__(self, df: pd.DataFrame):
    self.df = df.copy()
