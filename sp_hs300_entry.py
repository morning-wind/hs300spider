#coding:utf-8
from util import *
import demjson,datetime 


def spider_trade_day(range):
    import sp_hs300_trade_day as sp
    print '------------------spider_trade_day------------------'
    sp.spider_trade_day(range=range)
    
def spider_hs300_list():
    import sp_hs300list as sp
    print '------------------spider_hs300_list------------------'
    sp.spider_hs300list()
    
def spider_hs300_summary(stock_name,date):   
    import sp_hs300_day_summary as sp
    print '------------------spider_hs300_summary------------------'
    sp.spider_day_summary(stock_name, date)
    
def spider_hs300_detail(stock_name,date):   
    import sp_hs300_day_detail as sp
    print '------------------spider_hs300_detail------------------'
    sp.spider_day_detail(stock_name, date) 

#THE ENTRY POINT OF THE WHOLE SPIDER
def spider_entry():
    #spider_trade_day(range=90)
    #spider_hs300_list()
    hs_300list = hs300_list()
    last_trade_days = hs300_last_trade_day(count=90)
    for date in last_trade_days:
        print '-- date=%s'%date
        for stock_name in hs_300list:
            spider_hs300_summary(stock_name,date)
            #spider_hs300_detail(stock_name, date)

if __name__ == "__main__":
    spider_entry()