import pandas as pd
from division_rules.constrained_equal_awards_division import ConstrainedEqualAwardsDivision

claims = pd.DataFrame(
    data = {
        'claimant_id': [12, 13, 14, 15],
        'claim': [20, 10, 100, 200]
    }
)
estate = 100

div = ConstrainedEqualAwardsDivision(claims, estate)

div.check_claims()
div.execute_division()
div.check_result()
div.get_divided_results()
