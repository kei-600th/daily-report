from hand import Hand, UsersHand, CheatProgramHand


def determine_winner(users_hand, cheat_hand):
    if users_hand.beats == cheat_hand.name:
        return "あなたの勝ちです"
    elif users_hand.loses_to == cheat_hand.name:
        return "わたしの勝ちです"
    else:
        return "引き分けです"


def cheating_janken(users_input):
    if users_input not in Hand.HAND_PATTERN:
        print("グー、チョキ、パーのいずれかを入力してください。")
        return

    users_hand = UsersHand(users_input)
    users_hand.message()  # ユーザーの手を表示

    cheat_hand = CheatProgramHand(users_input)
    cheat_hand.message()  # チートプログラムの手を表示

    # 勝敗の判定と結果の表示
    result_message = determine_winner(users_hand, cheat_hand)
    print(result_message)


if __name__ == "__main__":
    users_input = input("グー、チョキ、パーのいずれかを入力してください：")
    cheating_janken(users_input)

