import pandas as pd

# レース保管クラス
class RaceBank:
  # コンストラクタ
  def __init__(self, pickle_path: str):
    self.__df = pd.read_pickle(pickle_path)