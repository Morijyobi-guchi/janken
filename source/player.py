def human_pon():
    # ユーザーの手を入力
    while True:
        user_input = (input("じゃんけんの手を選んでください（1: グー, 2: チョキ, 3: パー）："))
        if user_input == '1':
            return "グー"
        elif user_input == '2':
            return "チョキ"
        elif user_input == '3':
            return "パー"
        else:
            print("無効な入力です。1, 2, 3のいずれかを入力してください。")