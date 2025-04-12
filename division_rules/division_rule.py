from abc import ABC, abstractmethod
import pandas as pd

class DivisionRule(ABC):
    def __init__(self, claims: pd.DataFrame, estate: int):
        self.claims = claims
        self.check_claims()
        self.estate = estate
        self.result = None

    @abstractmethod
    def execute_division(self):
        pass

    def check_claims(self):
        assert (self.claims['claim'] >= 0).all(), "Some one came claiming negative, check: \n{}".format(self.result)
        print("Claims: \n{}".format(self.claims))

    def check_result(self):
        if not isinstance(self.result, pd.DataFrame):
            print("Divide the estate to generate results !")
            raise
        # Check efficiency
        assert self.result['result'].sum() == self.estate, \
            "Total assets divided between claimants is not equal to the total assets present. Check: \n{}".format(self.result)

        # check non negativity
        assert (self.result['result'] >= 0).all(), "Some one got negative assets, check: \n{}".format(self.result)

    def get_divided_results(self):
        print("Check the results after division: ")
        print(self.result if isinstance(self.result, pd.DataFrame) else "Divide first!")

