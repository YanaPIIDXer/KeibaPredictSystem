import pandas as pd

# マスタクラス
class Master:
  # コンストラクタ
  def __init__(self, pickle_root_path: str):
    self.__race_df = pd.read_pickle(pickle_root_path + '/races.pickle')
    self.__result_df = pd.read_pickle(pickle_root_path + '/results.pickle')
