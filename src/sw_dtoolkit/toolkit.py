from calculators.TestCalc1 import TestCalc1
from calculators.TestCalc2 import TestCalc2
from calculators.TestAdapter1 import TestAdapter1
from calculators.TestAdapter2 import TestAdapter2

class SWToolkit:
    def __init__(self):
      self.data = []
      self.calculators = []

      self.add('test1', 'Test Calculator 1', TestCalc1(), TestAdapter1())
      self.add('test2', 'Test Calculator 2', TestCalc2(), TestAdapter2())


    def add(self, calc_id, calc_desc, calculator, adapter):
        return 'hello from SWToolkit.add()'

    def calculate(self, calculator, swtInput):
        return 'hello from SWToolkit.calculate()'

    def listCalcs(self, calculator, swtInput):
        return 'hello from SWToolkit.listCalcs()'
