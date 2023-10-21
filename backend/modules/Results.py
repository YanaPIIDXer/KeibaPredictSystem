import pandas as pd

# 結果保管クラス
class ResultBank:
  # コンストラクタ
  def __init__(self, pickle_path: str):
    self.__df = pd.read_pickle(pickle_path)
    