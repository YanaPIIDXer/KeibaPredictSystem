import pandas as pd
from typing import List
from .horse import HorseBank

# レース情報クラス
class Race:
  # コンストラクタ
  def __init__(self, course: str, condition: str, horses: List[str]):
    self.__course = course
    self.__condition = condition
    self.__horses = horses

  # 学習・予測に必要なデータフレームを生成
  def build(self, horse_bank: HorseBank) -> pd.DataFrame:
    no = 1
    df_list = []
    for h_name in self.__horses:
      df = pd.DataFrame(index=[no])
      df['Name'] = h_name
      df['Course'] = self.__course
      df['Condition'] = self.__condition
      no += 1
      df_list.append(df)
    return pd.concat(df_list)

# レース情報保管クラス
class RaceBank:
  # コンストラクタ
  def __init__(self):
    self.__list = dict[str, Race]()

  # 追加
  def add(self, id: str, race: Race):
    self.__list[id] = race
    
  # 取得
  def get(self, id: str) -> Race:
    return self.__list[id]
  