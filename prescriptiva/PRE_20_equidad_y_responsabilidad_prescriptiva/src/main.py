from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
def audit(data):
    result=data.copy(); result['contact_rate']=result.contacted/result.eligible
    gap=result.groupby('policy').contact_rate.agg(lambda x:x.max()-x.min()).rename('contact_rate_gap')
    return result.merge(gap,on='policy')
def main(): audit(pd.read_csv(ROOT/'data'/'policy_impacts.csv')).to_csv(ROOT/'submission'/'equity_audit.csv',index=False)
if __name__=='__main__': main()
