class TestAdapter2:
    def __init__(self):
      self.data = []
      self.inputFields = []
      self.outputFields = []

    def validateInput(self, swtInput):
        return 'hello from TestAdapter2.validateInput()'

    def formatInput(self, swtInput):
        return 'hello from TestAdapter2.formatInput()'

    def validateOutput(self, swtOutput):
        return 'hello from TestAdapter2.validateOutput()'

    def formatOutput(self, swtOutput):
        return 'hello from TestAdapter2.formatOutput()'
