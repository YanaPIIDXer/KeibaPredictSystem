from typing import List

# レース情報クラス
class Race:
  # コンストラクタ
  def __init__(self, course: str, condition: str, horses: List[str]):
    self.course = course
    self.condition = condition
    self.horses = horses
