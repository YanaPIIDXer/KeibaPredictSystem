from .Race import RaceBank
from .Results import ResultBank

class MasterBank:
  def __init__(self, race_pickle_path, result_pickle_path):
    self.__race_bank = RaceBank(race_pickle_path)
    self.__result_bank = ResultBank(result_pickle_path)
