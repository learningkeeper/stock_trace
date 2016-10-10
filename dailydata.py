#!/usr/bin/python
#coding=utf-8
import sh


title = [ u"交易日期", u"成交股數", u"成交金額", u"開盤價", u"最高價", u"最低價", u"收盤價", u"漲跌價差" ,u"成交筆數"]

stock = [ (u"第一金", "data/2892.csv") , ( u"0050", "data/0050.csv"), ( u"0056", "data/0056.csv"), (u"中華電信", "data/2412.csv"), (u"合庫金", "data/5880.csv"), (u"中信金", "data/2891.csv")\
	(u'新保',"data/9925.csv"), (u'正新', "data/2105.csv")]

def check_stock(x):
    result = sh.tail('-1', x).split(',')
    return zip(title, result)


def main():
    with open('text.txt', 'w') as fd:
		for name, file in stock:
 		    fd.write(name.encode('utf-8') + "\n")
		    for  head, data in check_stock(file):
 			    fd.write(head.encode('utf-8') + " : " + data.encode('utf-8') + "\n")


if __name__ == "__main__":
	main()
