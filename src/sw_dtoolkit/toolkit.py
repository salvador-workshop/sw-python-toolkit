from .calculators.test_calculator_1 import TestCalculator1
from .calculators.test_calculator_2 import TestCalculator2
from .adapters.test_adapter_1 import TestAdapter1
from .adapters.test_adapter_2 import TestAdapter2

class SWDToolkit:
    def __init__(self):
      self.data = []

      self.calc_test1 = TestCalculator1()
      self.calc_test2 = TestCalculator2()

      self.adpt_test1 = TestAdapter1()
      self.adpt_test2 = TestAdapter2()

    def __findCalculator(self, calculator_id):
        if calculator_id == 'test1':
            return self.calc_test1
        elif calculator_id == 'test2':
            return self.calc_test2
        else:
            return None

    def calculate(self, calc_id, swt_input):
        target_calc = self.__findCalculator(calc_id)
        return target_calc.calculate(swt_input)

    def listCalcs(self):
        return 'hello from SWDToolkit.listCalcs()'
