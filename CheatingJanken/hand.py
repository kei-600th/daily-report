class Hand:
    HAND_PATTERN = ["グー", "チョキ", "パー"]

    @staticmethod
    def calculate_hand(users_input):
        index = Hand.HAND_PATTERN.index(users_input)
        name = Hand.HAND_PATTERN[index]
        beats = Hand.HAND_PATTERN[(index + 1) % 3]
        loses_to = Hand.HAND_PATTERN[(index - 1) % 3]
        return name, beats, loses_to

    def __init__(self, name, beats, loses_to):
        self.name = name
        self.beats = beats
        self.loses_to = loses_to


class UsersHand(Hand):
    def __init__(self, users_input):
        name, beats, loses_to = Hand.calculate_hand(users_input)
        super().__init__(name, beats, loses_to)

    def message(self):
        print(f"あなたの手は{self.name}です。")


class CheatProgramHand(Hand):
    def __init__(self, users_input):
        _, _, users_beats = Hand.calculate_hand(users_input)
        name, beats, loses_to = Hand.calculate_hand(users_beats)
        super().__init__(name, beats, loses_to)

    def message(self):
        print(f"わたしの手は{self.name}です。")
