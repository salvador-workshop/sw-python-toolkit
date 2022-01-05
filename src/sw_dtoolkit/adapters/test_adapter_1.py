class TestAdapter1:
    def __init__(self):
      self.data = []
      self.inputFields = []
      self.outputFields = []

    def validateInput(self, swtInput):
        return 'hello from TestAdapter1.validateInput()'

    def formatInput(self, swtInput):
        return 'hello from TestAdapter1.formatInput()'

    def validateOutput(self, swtOutput):
        return 'hello from TestAdapter1.validateOutput()'

    def formatOutput(self, swtOutput):
        return 'hello from TestAdapter1.formatOutput()'
