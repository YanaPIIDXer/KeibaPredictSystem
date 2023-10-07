import pandas as pd
from typing import List
from .horse import HorseBank

# レース情報クラス
class Race:
  # コンストラクタ
  def __init__(self, course: str, condition: str, horses: List[str]):
    self.course = course
    self.condition = condition
    self.horses = horses

  # データ構築
  def build(self, bank: HorseBank) -> pd.DataFrame:
    df_list = []
    index = 0
    for name in self.horses:
      df = bank.get(name).data_frame()
      # 近走３走の平均
      # 上がり３ハロン
      t_falong = df.tail(3)['3Falong'].values.mean()
      # 最終コーナーの位置取り
      last_corner = df.tail(3)['LastCorner'].values.mean()
      row = {
        'No': index + 1,
        'Name': name,
        '3FalongMean': t_falong,
        'LastCornerMean': last_corner,
      }
      index += 1
      df_list.append(pd.DataFrame(row, index=[row['No']]))
    return pd.concat(df_list)
