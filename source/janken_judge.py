def judge(cpu_hand, user_hand):
    # CPUとユーザーの手を比較し、勝敗を判定
    if cpu_hand == user_hand:
        return "引き分け"
    elif (cpu_hand == "グー" and user_hand == "チョキ") or \
         (cpu_hand == "チョキ" and user_hand == "パー") or \
         (cpu_hand == "パー" and user_hand == "グー"):
        return "CPUの勝ち"
    else:
        return "ユーザの勝ち"


