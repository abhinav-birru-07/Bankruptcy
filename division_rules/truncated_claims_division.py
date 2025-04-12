from division_rules.division_rule import DivisionRule


class TruncatedClaimsDivision(DivisionRule):

    def execute_division(self):
        self.result = self.claims.assign(result=self.claims['claim'].apply(lambda x: min(x, self.estate)))
        r = self.estate / self.result['result'].sum()
        self.result['result'] *= r
        self.check_result()


