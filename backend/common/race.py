import pandas as pd

# レース情報クラス
class Race:
  # コンストラクタ
  def __init__(self, df: pd.DataFrame):
    self.df = df.copy()
