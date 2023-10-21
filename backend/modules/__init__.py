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
  
  # 結果情報をレースIDにマージ
  def merge_result_to_race(self, race_df: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(race_df, self.__result_df, on='RaceID', how='inner')

    def calc_vars(group):
      group = group.sort_values('Date')
      group['3FalongMean'] = group['3Falong'].expanding().mean().shift(1)
      group['ArrivalMean'] = group['Arrival'].expanding().mean().shift(1)
      group['3FalongMeanByCondition'] = group[group['Condition'] == group['Condition'].iloc[-1]]['3Falong'].expanding().mean().shift(1)
      return group
    
    df = df.groupby('Name').apply(calc_vars).reset_index(drop=True).sort_values(['Date', 'RaceNo', 'No'])

    df['3FalongMeanByRaceID'] = df.groupby('RaceID')['3FalongMean'].transform('mean')
    df['Adjust3FalongMean'] = df['3FalongMean'] - df['3FalongMeanByRaceID']
    df['ArrivalMeanByRaceID'] = df.groupby('RaceID')['ArrivalMean'].transform('mean')
    df['3FalongMeanByRaceID'] = df.groupby('RaceID')['3FalongMeanByCondition'].transform('mean')
    df['Adjust3FalongMeanByCondition'] = df['3FalongMeanByRaceID'] - df['3FalongMeanByCondition']
    df['Adjust3ArrivalMean'] = df['ArrivalMean'] - df['ArrivalMeanByRaceID']
    
    return df
  