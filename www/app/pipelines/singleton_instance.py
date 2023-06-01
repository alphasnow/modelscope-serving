class SingletonInstance:
    _instance = None
    _singleton = True

    def __init__(self, singleton: bool = True):
        self._singleton = singleton

    def build(self):
        pass

    def instance(self):
        # if not self._singleton:
        #     return self.build()
        # if self._instance is None:
        #     raise ValueError("SingletonInstance is not initialize")
        # return self._instance

        if self._singleton and self._instance is not None:
            return self._instance
        return self.build()

    def initialize(self):
        if not self._singleton:
            return
        self._instance = self.build()

    # def handle(self):
    #     pass
