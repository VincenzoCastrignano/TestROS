class Agent4:
    def __init__(self,valence_table):
        """ Creating our agent """
        self.valence_table = valence_table
        self._action = None
        self.previous_action = 0
        self.anticipated_outcome = None
        self.previous_outcome = 0
        self.outcome_for_action1 = None
        self.outcome_for_action0 = 0
        self.cpt = 0

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
        elif self.cpt == 0 and self._action is not None:
            self.outcome_for_action0 = outcome
            self._action = 1
            self.anticipated_outcome = 1
            self.cpt = 1
        elif self.cpt == 1 and self._action == 1:
            self.outcome_for_action1 = outcome
            self.cpt = 2

        elif self.cpt == 2:
            valence0 = self.valence_table[0][self.outcome_for_action0]
            valence1 = self.valence_table[1][self.outcome_for_action1]

            if valence1 == -1:
                self._action = 0
                self.anticipated_outcome = self.outcome_for_action0
            elif valence0 == -1:
                self._action = 1
                self.anticipated_outcome = self.outcome_for_action1


        return self._action
