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
    self.__df['LastCorner'] = self.__df['LastCorner'].transform(lambda x: x.rolling(3, min_periods=1).mean().shift(1))

  # 学習・予測に必要なデータを生成
  def build(self, condition: str) -> object:
    return {
      'ArrivalAvg': self.__df.tail(1)['ArrivalAvg'].values[0],
      '3FalongAvg': self.__df.tail(1)['3FalongAvg'].values[0],
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
