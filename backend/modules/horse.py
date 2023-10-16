import pandas as pd

# 馬情報クラス
class Horse:
  # コンストラクタ
  def __init__(self, df: pd.DataFrame):
    self.__df = df.copy().sort_values('Date')
    # 最終コーナーの位置取りの平均から脚質を決定する
    self.__leg_type = Horse.__position_to_leg_type(self.__df['LastCorner'].mean())

  # 学習・予測に必要なデータを生成
  def build(self, course: str, condition: str) -> object:
    return {
      'LegType': self.__leg_type,
    }
  
  # 位置取りを脚質に変換
  def __position_to_leg_type(position: float) -> str:
    if position <= 2.0: return '逃げ'
    if position <= 5.0: return '先行'
    if position <= 8.0: return '差し'
    return '追込'

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
