import pandas as pd
from typing import List
import numpy as np

# レースクラス
class Race:
  # コンストラクタ
  def __init__(self, df):
    self.__df = df

# レース保管クラス
class RaceBank:
  # コンストラクタ
  def __init__(self, pickle_path: str):
    self.__df = pd.read_pickle(pickle_path)

  # 期間を指定して取得
  def get_by_period(self, start: str, end: str) -> List[Race]:
    df = self.__df[(self.__df['Date'] >= start) & (self.__df['Date'] <= end)]
    races = []
    df_list = np.array_split(df, len(df))
    for d in df_list:
      races.append(Race(d))
    return races
  
  # 取得
  def get(self, id: str) -> Race:
    return Race(self.__df[self.__df['RaceID'] == id])
