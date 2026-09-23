from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
def main():
 d=pd.read_csv(ROOT/'data'/'recommendation.csv'); d['owner']='Dirección de operaciones'; d.to_csv(ROOT/'submission'/'policy_brief.csv',index=False)
if __name__=='__main__': main()
