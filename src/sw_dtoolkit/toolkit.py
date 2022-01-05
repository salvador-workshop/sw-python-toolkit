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
        newCalc = {'id': calc_id, 'desc': calc_desc, 'calculator': calculator, 'adapter': adapter}
        self.calculators.append(newCalc)
        return 0

    def calculate(self, calculator, swtInput):
        return self.calculators[0].calculator.calculate(swtInput)

    def listCalcs(self, calculator, swtInput):
        return 'hello from SWToolkit.listCalcs()'
