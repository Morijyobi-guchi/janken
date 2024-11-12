import player
import computer
import janken_judge
import random

def human_pon():
    # ユーザーの手を入力
    while True:
        user_input = input("じゃんけんの手を選んでください（1: グー, 2: チョキ, 3: パー）：")
        if user_input == '1':
            return "グー"
        elif user_input == '2':
            return "チョキ"
        elif user_input == '3':
            return "パー"
        else:
            print("無効な入力です。1, 2, 3のいずれかを入力してください。")

def cpu_pon():
    # CPUの手をランダムに選択
    cpu_choice = random.choice([1, 2, 3])
    if cpu_choice == 1:
        return "グー"
    elif cpu_choice == 2:
        return "チョキ"
    else:
        return "パー"

def janken_main():
    # 勝敗数のカウント
    user_wins = 0
    cpu_wins = 0

    # 3回のじゃんけんを行う
    for i in range(3):
        print(f"\n----- ラウンド {i + 1} -----")

        # ユーザーとCPUの手を取得
        user_hand = human_pon()
        cpu_hand = cpu_pon()

        # ユーザーとCPUの手を表示
        print(f"あなたの手：{user_hand}")
        print(f"コンピュータの手：{cpu_hand}")

        # 勝敗の判定
        result = judge(cpu_hand, user_hand)
        print("結果:", result)

        # 勝敗のカウント
        if result == "ユーザの勝ち":
            user_wins += 1
        elif result == "CPUの勝ち":
            cpu_wins += 1

    # 最終結果の表示
    print("\n----- 最終結果 -----")
    print(f"あなたの勝ち数: {user_wins}")
    print(f"コンピュータの勝ち数: {cpu_wins}")

    # 総合勝敗の判定
    if user_wins > cpu_wins:
        print("あなたの総合勝利です！")
    elif cpu_wins > user_wins:
        print("コンピュータの総合勝利です！")
    else:
        print("引き分けです！")

if __name__ == '__main__':

      janken_main()