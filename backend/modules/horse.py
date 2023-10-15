import pandas as pd

# 馬情報クラス
class Horse:
  # コンストラクタ
  def __init__(self, df: pd.DataFrame):
    self.__df = df.copy().sort_values('Date')
    # 過去３走の平均着順
    self.__df['ArrivalAvg'] = self.__df['Arrival'].transform(lambda x: x.rolling(3, min_periods=1).mean().shift(1))
    # 過去３走の上がり３ハロン平均
    self.__df['3FalongAvg'] = self.__df['3Falong'].transform(lambda x: x.rolling(3, min_periods=1).mean().shift(1))
    # 過去３走の最終コーナーの位置取り平均
    self.__df['LastCornerAvg'] = self.__df['LastCorner'].transform(lambda x: x.rolling(3, min_periods=1).mean().shift(1))
    self.__cond_dfs = dict()

  # 学習・予測に必要なデータを生成
  def build(self, condition: str) -> object:
    if not condition in self.__cond_dfs:
      cond_df = self.__df[self.__df['Condition'] == condition].copy()
      self.__cond_dfs[condition] = cond_df
      # 引数に取った馬場状態と同じ馬場状態の過去３走分の上がり３ハロン
      cond_df['Condition3FalongAvg'] = cond_df['3Falong'].transform(lambda x: x.rolling(3, min_periods=1).mean().shift(1))
    else:
      cond_df = self.__cond_dfs[condition]
    
    return {
      'ArrivalAvg': self.__df.tail(1)['ArrivalAvg'].values[0],
      '3FalongAvg': self.__df.tail(1)['3FalongAvg'].values[0],
      'LastCornerAvg': self.__df.tail(1)['LastCornerAvg'].values[0],
      'Condition3FalongAvg': cond_df.tail(1)['Condition3FalongAvg'].values[0] if not cond_df.empty else None,
    }

# 馬情報保管クラス
class HorseBank:
  # コンストラクタ
  def __init__(self):
    self.__list = dict[str, Horse]()

  # 追加
  def add(self, name: str, horse: Horse):
    self.__list[name] = horse

  # 取得
  def get(self, name: str) -> Horse:
    return self.__list[name]
