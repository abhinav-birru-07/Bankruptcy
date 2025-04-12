from division_rules.division_rule import DivisionRule

class ProportionalDivision(DivisionRule):

    def execute_division(self):
        r = self.estate / self.claims['claim'].sum()
        self.result = self.claims.assign(result = self.claims['claim']*r)
        self.check_result()

