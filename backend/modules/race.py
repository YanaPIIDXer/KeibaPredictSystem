import pandas as pd
from typing import List
from .horse import HorseBank

# レースに出走する馬の情報
class RaceHorse:
  def __init__(self, name: str, jockey: str):
    self.name = name
    self.jockey = jockey

# レース情報クラス
class Race:
  # コンストラクタ
  def __init__(self, course: str, condition: str, horse_infos: List):
    self.__course = course
    self.__condition = condition
    self.__horse_infos = horse_infos
    self.__result = None

  # 学習用の結果を設定
  def set_result(self, first: int, second: int, third: int):
    self.__result = [first, second, third]

  # 学習・予測に必要なデータフレームを生成
  def build(self, horse_bank: HorseBank) -> pd.DataFrame:
    no = 1
    data_list = []
    for info in self.__horse_infos:
      data = {}
      name = info[0]
      jockey = info[1]
      horse_data = horse_bank.get(name).build(self.__condition)
      data['No'] = no
      data['Name'] = name
      data['Course'] = self.__course
      data['Condition'] = self.__condition
      data['Jockey'] = jockey
      data['ArrivalAvg'] = horse_data['ArrivalAvg']
      data['3FalongAvg'] = horse_data['3FalongAvg']
      if self.__result != None:
        data['IsPlace'] = 1 if no in self.__result else 0
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
  