from division_rules.division_rule import DivisionRule


class ConstrainedEqualAwardsDivision(DivisionRule):

    def execute_division(self):
        self.result = self.claims.copy()
        self.result.sort_values(by=['claim'])
        ct = 0
        given = 0
        self.result['result'] = None
        for idx, row in self.result.iterrows():
            avg = (self.estate-given) / (len(self.claims)-ct)
            if row['claim'] < avg:
                self.result.loc[idx, 'result'] = self.result.loc[idx, 'claim']
            else:
                self.result.loc[idx, 'result'] = avg
            given += self.result.loc[idx, 'result']
            ct += 1
        self.result.sort_index(inplace=True)
        self.check_result()



