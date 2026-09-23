from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
def evaluate(orders, scenarios):
    rows=[]
    for order in orders.itertuples(index=False):
        sold=scenarios.demand.clip(upper=order.order_quantity)
        leftover=(order.order_quantity-scenarios.demand).clip(lower=0)
        value=sold*order.price-order.order_quantity*order.unit_cost-leftover*order.disposal_cost
        rows.append({"order_quantity":order.order_quantity,"expected_value":(value*scenarios.probability).sum(),"stockout_probability":scenarios.loc[scenarios.demand>order.order_quantity,"probability"].sum()})
    return pd.DataFrame(rows)
def main():
    evaluate(pd.read_csv(ROOT/'data'/'order_options.csv'),pd.read_csv(ROOT/'data'/'forecast_scenarios.csv')).to_csv(ROOT/'submission'/'order_comparison.csv',index=False)
if __name__=='__main__': main()
