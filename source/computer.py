import random
def cpu_pon():
    # CPUの手をランダムに選択
    cpu_choice = random.choice([1, 2, 3])
    if cpu_choice == 1:
        return "グー"
    elif cpu_choice == 2:
        return "チョキ"
    else:
        return "パー"
    
