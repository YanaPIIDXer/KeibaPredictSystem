from .Race import RaceBank, Race
from .Results import ResultBank, Result
from typing import List

# 複数のマスタを統合して扱うマスタクラス
class MasterBank:
  # コンストラクタ
  def __init__(self, race_pickle_path, result_pickle_path):
    self.__race_bank = RaceBank(race_pickle_path)
    self.__result_bank = ResultBank(result_pickle_path)

  # 期間を指定したレース情報取得
  def get_race_by_period(self, start: str = '2000-01-01', end: str = '2999-12-31') -> List[Race]:
    return self.__race_bank.get_by_period(start, end)

  # 指定したIDのレースを取得
  def get_race(self, id: str) -> Race:
    return self.__race_bank.get(id)
  
  # 指定したレースIDの結果を取得
  def get_result(self, race_id: str) -> Result:
    return self.__result_bank.get(race_id)
