from site import Site

class System():
    def __init__(self):
        self.site = Site()

    def viable_inverters(self):

        return 0

    def viable_modules(self):

        return 0

    def decision_making(self):
        for inverter in self.viable_inverters():
            for module in self.viable_modules():
                return 1