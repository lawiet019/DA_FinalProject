import baostock as bs
import pandas as pd

# log in
lg = bs.login()
# set response data of login
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)
# set parameters
startdate = '2020-01-01'
enddate = '2020-12-31'


# get the first layer of data from shenzhen
rs = bs.query_history_k_data_plus("sh.000001",
    "date,code,open,high,low,close,preclose,volume,amount,pctChg",
    start_date=startdate, end_date=enddate, frequency="d")
print('query_history_k_data_plus respond error_code:'+rs.error_code)
print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)

# keep the result in list
data_list = []
while (rs.error_code == '0') & rs.next():
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)
# save the data to csv
result.to_csv("/Users/koko/Documents/data_analytics/finalproject/data/stock_shanghai_all.csv", index=False)
print(result)


code_list = ["sh.000032","sh.000033","sh.000034","sh.000035","sh.000036","sh.000037","sh.000038",
             "sh.000039","sh.000040","sh.000041","sh.000104","sh.000105","sh.000106","sh.000107",
             "sh.000108","sh.000109","sh.000110","sh.000111","sh.000112","sh.000113"]
second_list = []
for code in code_list:
    rs = bs.query_history_k_data_plus(code,
                                      "date,code,open,high,low,close,preclose,volume,amount,pctChg",
                                      start_date=startdate, end_date=enddate, frequency="d")
    while (rs.error_code == '0') & rs.next():
        second_list.append(rs.get_row_data())
result = pd.DataFrame(second_list, columns=rs.fields)
result.to_csv("/Users/koko/Documents/data_analytics/finalproject/data/stock_firstindex_all.csv", index=False)
print(result)

bs.logout()
