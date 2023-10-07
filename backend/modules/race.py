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
    data_list = []
    for h_name in self.__horses:
      data = {}
      horse_data = horse_bank.get(h_name).build(self.__condition)
      data['No'] = no
      data['Name'] = h_name
      data['Course'] = self.__course
      data['Condition'] = self.__condition
      data['ArrivalAvg'] = horse_data['ArrivalAvg']
      data['3FalongAvg'] = horse_data['3FalongAvg']
      no += 1
      data_list.append(data)
    return pd.DataFrame(data_list)

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
  
  # 全取得
  def get_all(self) -> List[Race]:
    list = []
    for _, race in self.__list.items():
      list.append(race)
    return list
  