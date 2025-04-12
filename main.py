import argparse
import pandas as pd


def proportional_division(claims, estate):
    r = estate / claims.sum()
    res = claims.apply(lambda x: x*r)
    return res


def truncated_claims(claims, estate):
    truncated = claims.apply(lambda x: min(x, estate))
    res = proportional_division(truncated, estate)
    return res


def constrained_equal_awards(claims, estate):
    r = estate / len(claims)
    claims = claims.sort_values()
    out = {}
    given = 0
    ct = 0
    for idx, cl in claims.items():
        r = (estate - given) / (len(claims) - ct)
        if cl < r:
            out[idx] = cl
            claims[idx] = 0
            given += cl
        else:
            out[idx] = r
            claims[idx] = 0
            given += r
        ct += 1
    return pd.Series(data=out).sort_index()


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--claims', type=int, nargs='+', help='a list of claims', required=True)
    parser.add_argument('--estate', type=int, required=True)
    parser.add_argument('--rule_for_division', choices=['proportional_division', 'truncated_claims', 'constrained_equal_awards'])
    args = parser.parse_args()
    claims = pd.Series(args.claims)
    estate = args.estate
    rule_for_division = args.rule_for_division
    print(f"Claims provided - \n{claims}")
    print(f"Estate provided - \n{estate}")
    print(f"Rule provided - \n{rule_for_division}")
    print(globals()[rule_for_division](claims, estate))
