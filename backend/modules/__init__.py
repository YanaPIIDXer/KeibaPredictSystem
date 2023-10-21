import pandas as pd

# マスタクラス
class Master:
  # コンストラクタ
  def __init__(self, pickle_root_path: str):
    self.__race_df = pd.read_pickle(pickle_root_path + '/races.pickle')
    self.__result_df = pd.read_pickle(pickle_root_path + '/results.pickle')

  # 期間を指定してレース情報を取得
  def get_race_by_period(self, start: str = '1990-01-01', end: str = '2999-12-31') -> pd.DataFrame:
    return self.__race_df[(self.__race_df['Date'] >= start) & (self.__race_df['Date'] <= end)].copy()

  # IDを指定してレース情報を取得
  def get_race_by_id(self, id: str) -> pd.DataFrame:
    return self.__race_df[self.__race_df['RaceID'] == id].copy()
