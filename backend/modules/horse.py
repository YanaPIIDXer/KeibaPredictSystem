import pandas as pd

# 馬情報クラス
class Horse:
  # コンストラクタ
  def __init__(self, df: pd.DataFrame):
    self.__df = df.copy().sort_values('Date')

  # 事前処理したDataFrameを返す
  def preprocess(self) -> pd.DataFrame:
    df = self.__df.copy()

    # 過去３走の平均着順
    df['ArrivalAvg'] = df['Arrival'].transform(lambda x: x.rolling(3, min_periods=1).mean().shift(1))
    
    return df

# 馬情報保管クラス
class HorseBank:
  # コンストラクタ
  def __init__(self):
    self.__list = dict[str, Horse]()

  # 追加
  def add(self, name: str, horse: Horse):
    self.__list[name] = horse

  # 取得
  def get(self, name: str) -> Horse:
    return self.__list[name]
