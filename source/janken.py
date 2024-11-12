
import computer
import player
import janken_judge

def janken_main():
    # 勝敗数のカウント
    user_wins = 0
    cpu_wins = 0

    # 3回のじゃんけんを行う
    for i in range(3):
        print(f"\n----- ラウンド {i + 1} -----")

        # ユーザーとCPUの手を取得
        user_hand = player.human_pon()
        cpu_hand = computer.cpu_pon()

        # ユーザーとCPUの手を表示
        print(f"あなたの手：{user_hand}")
        print(f"コンピュータの手：{cpu_hand}")

        # 勝敗の判定
        result = janken_judge.judge(cpu_hand, user_hand)
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

# メイン関数の実行

if __name__ == '__main__':
    janken_main()