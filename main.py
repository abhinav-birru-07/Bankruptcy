import argparse
import pandas as pd
from division_rules.proportional_division import ProportionalDivision
from division_rules.constrained_equal_awards_division import ConstrainedEqualAwardsDivision
from division_rules.truncated_claims_division import TruncatedClaimsDivision


if __name__=='__main__':
    '''
    Sample run config:
    --claimant_ids 11 12 13 14 --estate 100 --claims 10 100 20 200 --rule_for_division ConstrainedEqualAwardsDivision
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--claimant_ids', nargs='+', required=False, default=None)
    parser.add_argument('--claims', type=int, nargs='+', help='a list of claims', required=True)
    parser.add_argument('--estate', type=int, required=True)
    parser.add_argument('--rule_for_division',
                        choices=['ProportionalDivision', 'TruncatedClaimsDivision', 'ConstrainedEqualAwardsDivision'])
    args = parser.parse_args()
    claims = args.claims
    claimant_ids = args.claimant_ids if args.claimant_ids else [x+1 for x in range(len(claims))]
    estate = args.estate
    rule_for_division = args.rule_for_division
    claims_df = pd.DataFrame(data = {
        'claimant_ids': claimant_ids,
        'claim': claims
    })
    # print(f"Claims provided - \n{claims}")
    # print(f"Estate provided - \n{estate}")
    print(f"Rule provided - \n{rule_for_division}")
    div = globals()[rule_for_division](claims_df, estate)
    div.check_claims()
    div.execute_division()
    div.check_result()
    div.get_divided_results()
