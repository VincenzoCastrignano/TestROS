class Agent3:
    def __init__(self, valence_table):
        """ Creating our agent """
        self.valence_table = valence_table
        self._action = None
        self.anticipated_outcome = None
        self.cycle = 0
        self.data_oc = None
        self.data_oc2 = None
        self.anticipated_outcome = None
        self.etat = "Content"

    def action(self, outcome):
        print(self.valence_table[self._action][outcome])
        """ tracing the previous cycle """
        if self._action is not None:
            print("Action: " + str(self._action) +
                  ", Anticipation: " + str(self.anticipated_outcome) +
                  ", Outcome: " + str(outcome) +
                  ", Satisfaction: (anticipation: " + str(self.anticipated_outcome == outcome) +
                  ", Etat: " + str(self.etat) + ")" +
                  ", valence: " + str(self.valence_table[self._action][outcome]) + ")" +
                  " (deuxième valeur précédente : " + str(self.data_oc) +
                  ", valeur précédente : " + str(self.data_oc2) + ")")

        """ Computing the next action to enact """
        # TODO: Implement the agent's decision mechanism
        # print("valence : " + str(self.valence_table[self._action][outcome]))
        if self._action == 0:
            self.data_oc = outcome
            self._action = 1
        else:
            self.data_oc2 = outcome
            self._action = 0

        if self._action == 0:
            self.anticipated_outcome = self.data_oc
        else:
            self.anticipated_outcome = self.data_oc2

        if self.anticipated_outcome == outcome:
            self.etat = 'Ennui'
        else:
            self.etat = 'Content'

        # TODO: Implement the agent's anticipation mechanism
        return self._action