import pandas as pd

# 結果クラス
class Result:
  # コンストラクタ
  def __init__(self, df):
    self.__df = df

# 結果保管クラス
class ResultBank:
  # コンストラクタ
  def __init__(self, pickle_path: str):
    self.__df = pd.read_pickle(pickle_path)
    
  # 取得
  def get(self, race_id: str) -> Result:
    return Result(self.__df[self.__df['RaceID'] == race_id])
