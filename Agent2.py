#!/usr/bin/env python
import random
from turtlepy_enacter import TurtlePyEnacter


# from Agent5 import Agent5
# from OsoyooCarEnacter import OsoyooCarEnacter

class Agent2:
    def __init__(self, _hedonist_table):
        """ Creating our agent """
        self.hedonist_table = _hedonist_table
        self._action = None
        self.anticipated_outcome = None
        self.cycle = 0
        self.data_oc = None
        self.data_oc2 = None
        self.anticipated_outcome = None
        self.etat = "Content"

    def action(self, outcome):
        """ tracing the previous cycle """
        if self._action is not None:
            print("Action: " + str(self._action) +
                  ", Anticipation: " + str(self.anticipated_outcome) +
                  ", Outcome: " + str(outcome) +
                  ", Satisfaction: (anticipation: " + str(self.anticipated_outcome == outcome) +
                  ", Etat: " + str(self.etat) + ")" +
                  ", valence: " + str(self.hedonist_table[self._action][outcome]) + ")" +
                  " (deuxième valeur précédente : " + str(self.data_oc) +
                  ", valeur précédente : " + str(self.data_oc2) + ")")

        """ Computing the next action to enact """
        # TODO: Implement the agent's decision mechanism
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
        # if self.anticipated_outcome == 0:
        #     self._action = 0
        # if self.anticipated_outcome == 1:
        #     print("ahah")
        #     self._action = 1
        #
        #
        # elif self.data_oc is None:
        #     self._action = 1
        #     self.data_oc = outcome
        # elif self.data_oc2 is None and self.data_oc is not None:
        #     self.data_oc2 = outcome
        #     self._action = 0
        # else:
        #     if self._action == 0 and self.data_oc2 == 1:
        #         self.anticipated_outcome = 0
        #         self.etat = "Pas content"
        #         self.data_oc2 = self.data_oc
        #         self.data_oc = outcome
        #     if self._action == 0 and self.data_oc == 0:
        #         self.anticipated_outcome = 0
        #         self.data_oc2 = self.data_oc
        #         self.data_oc = outcome
        #     if self._action == 1 and self.data_oc2 == 1:
        #         self.anticipated_outcome = 1
        #         self.data_oc2 = self.data_oc
        #         self.data_oc = outcome
        #     if self._action == 1 and self.data_oc == 0:
        #         self.anticipated_outcome = 0
        #         self.data_oc2 = self.data_oc
        #         self.data_oc = outcome



        # TODO: Implement the agent's anticipation mechanism
        return self._action


class Environment1:
    """ In Environment 1, action 0 yields outcome 0, action 1 yields outcome 1 """

    def outcome(self, action):
        # return int(input("entre 0 1 ou 2"))
        if action == 0:
            return 0
        else:
            return 1


class Environment2:
    """ In Environment 2, action 0 yields outcome 1, action 1 yields outcome 0 """

    def outcome(self, action):
        if action == 0:
            return 1
        else:
            return 0


class Environment3:
    """ Environment 3 yields outcome 1 only when the agent alternates actions 0 and 1 """

    def __init__(self):
        """ Initializing Environment3 """
        self.previous_action = 0

    def outcome(self, action):
        _outcome = 1
        if action == self.previous_action:
            _outcome = 0
        self.previous_action = action
        return _outcome


class Environment4:
    def outcome(self):
        return random.randint(0, 1)


# TODO Define the hedonist valance of interactions (action, outcome)
hedonist_table = [[-1, 1], [-1, 1]]
# TODO Choose an agent
a = Agent2(hedonist_table)
# a = Agent5(hedonist_table)
# TODO Choose an environment
e = Environment3()
# e = Environment2()
# e = Environment3()
# e = TurtleSimEnacter()
# e = TurtlePyEnacter()
# e = OsoyooCarEnacter()

if __name__ == '__main__':
    """ The main loop controlling the interaction of the agent with the environment """
    outcome = 0
    for i in range(70):
        action = a.action(outcome)
        outcome = e.outcome(action)
