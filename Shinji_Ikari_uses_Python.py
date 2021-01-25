
import time

#関数switchを定義
def switch():
  print("ｶﾁｯ…")
  time.sleep(0.5)
  print("ﾋﾞｭｲｨｲｲｲﾝ…")
  time.sleep(0.5)
  print("ﾊﾞｧﾝ!!")
  time.sleep(0.5)

#目標の数を入力する
input = input("目標の数を入力してください。")

#目標の数が最大で18になるように調整する
if int(input) <= 18 and int(input) >= 0:
    mokuhyou = int(input)
else:
    mokuhyou = 18

#目標をセンターに入れてスイッチ
for center in range(mokuhyou):
  switch()

