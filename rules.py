from sys import argv
import pandas as pd
import numpy as np


#unit price analysis
#paying over or under market value for a product
#Adjust for seasonality - summer lower, winter higher
#Adjust for currency strength:
#    primarily in raw goods
#    Todo: look into other goods that are strongly effected by currency strength
#    Account for time-biased goods, IE inflation, advances in technology, trends
#
#ref_prices is a rolling mean, indexed by year and quarter

ref_prices = {"1990":{"q1":200,"q2":150,"q3":500,"q4":620}}
def unit_price(price,ref_prices,year,quarter,severity=1):
    ref_arr = np.array(ref_prices[year][quarter])
    if price < ref_arr.mean - ref_arr.std*severity or price > ref_arr.mean + ref_arry.std*severity:
        return True #means warrants further investigation
    else:
        return False #means we don't expect further investigation needed

def main():
    apply_rules()

if __name__ == '__main__':
    df = pd.DataFrame.from_csv(argv[1])
    main(df)
