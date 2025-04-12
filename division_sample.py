import pandas as pd
from division_rules.constrained_equal_awards_division import ConstrainedEqualAwardsDivision
from division_rules.proportional_division import ProportionalDivision
from division_rules.truncated_claims_division import TruncatedClaimsDivision

claims = pd.DataFrame(
    data = {
        'claimant_id': [12, 13, 14, 15],
        'claim': [20, 10, 100, 200]
    }
)
estate = 100

div = TruncatedClaimsDivision(claims, estate)

div.check_claims()
div.execute_division()
div.check_result()
div.get_divided_results()
