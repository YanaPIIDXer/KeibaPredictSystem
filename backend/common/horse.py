import pandas as pd

# 馬情報クラス
class Horse:
  # コンストラクタ
  def __init__(self, df: pd.DataFrame):
    self.__df = df.copy()
    self.__df.sort_values('Date')

  # データフレーム取得
  def data_frame(self) -> pd.DataFrame:
    return self.__df.copy()

# 全ての馬情報を格納するクラス
class HorseBank:
  # コンストラクタ
  def __init__(self, df: pd.DataFrame):
    self.horses = dict()
    group = df.groupby('Name')
    for name, h_df in group:
      self.horses[name] = Horse(h_df)

  # 指定した馬名の情報を取得
  def get(self, name: str) -> Horse:
    return self.horses.get(name)
