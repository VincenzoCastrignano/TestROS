import random


class Agent4:
    def __init__(self, valence_table):
        """ Creating our agent """
        self.valence_table = valence_table
        self._action = None
        self.previous_action = 0
        self.anticipated_outcome = None
        self.previous_outcome = 0
        self.outcome_for_action0 = None
        self.outcome_for_action1 = None
        self.outcome_for_action2 = None

    def action(self, outcome):
        """ tracing the previous cycle """
        if self._action is not None:
            print("Action: " + str(self._action) +
                  ", Anticipation: " + str(self.anticipated_outcome) +
                  ", Outcome: " + str(outcome) +
                  ", Satisfaction: (anticipation: " + str(self.anticipated_outcome == outcome) +
                  ", valence: " + str(self.valence_table[self._action][outcome]) + ")")

        if self._action is None:
            self._action = 0
            self.outcome_for_action0 = outcome
            self.anticipated_outcome = 1
        else:
            match self._action:
                case 0:
                    self.outcome_for_action0 = outcome
                    valence0 = self.valence_table[0][self.outcome_for_action0]
                    if valence0 == -1:
                        self._action = random.randint(1, 2)
                        self.anticipated_outcome = self.outcome_for_action0
                case 1:
                    self.outcome_for_action1 = outcome
                    valence1 = self.valence_table[1][self.outcome_for_action1]
                    if valence1 == 1:
                        self._action = 0
                        self.anticipated_outcome = self.outcome_for_action1
                case 2:
                    self.outcome_for_action2 = outcome
                    valence2 = self.valence_table[2][self.outcome_for_action2]
                    if valence2 == 1:
                        self._action = 0
                        self.anticipated_outcome = self.outcome_for_action2
                case _:
                    print("default")
                    pass

        return self._action
