import pandas as pd
from typing import List

# レース情報クラス
class Race:
  # コンストラクタ
  def __init__(self, course: str, condition: str, horses: List[str]):
    self.__course = course
    self.__condition = condition
    self.__horses = horses

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
  