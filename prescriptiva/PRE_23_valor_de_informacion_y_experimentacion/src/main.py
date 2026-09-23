from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
def evaluate(scenarios, study_cost=8000, accuracy=0.85):
    launch_now=(scenarios.probability*scenarios.launch_value).sum()
    prior_positive=scenarios.loc[scenarios.launch_value>0,'probability'].sum()
    informed=prior_positive*120000*accuracy+(1-prior_positive)*0
    return pd.DataFrame([{'action':'lanzar_ahora','expected_value':launch_now},{'action':'medir_antes','expected_value':informed-study_cost}])
def main(): evaluate(pd.read_csv(ROOT/'data'/'decision_scenarios.csv')).to_csv(ROOT/'submission'/'information_value.csv',index=False)
if __name__=='__main__': main()
