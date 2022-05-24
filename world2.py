self._action = None
        self.anticipated_outcome = None
        self.cycle = 0
        self.data = None
        self.etat = "Content"
", Etat: " + str(self.etat) +
", Cycle : " + str(self.cycle) +
        if self._action is None:
            self._action = 0
        if self.data != outcome:
            print("Différent ! restart")
            self.cycle = 1
            self.data = outcome
        if self.cycle < 5:
            self.data = outcome
            self.etat = "Content"
            self.cycle += 1
        if self.cycle == 4:
            self.etat = "Ennui"
        if self.etat == "Ennui":
            if self._action == 0:
                print("Switch action to 1")
                self._action = 1
                self.cycle = 0
            elif self._action == 1:
                print("Switch action to 0")
                self._action = 0
                self.cycle = 0
class Environment4:
    def outcome(self):
        return random.randint(0, 1)