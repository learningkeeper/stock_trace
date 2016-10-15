# tsec

- [原作者連結](https://github.com/Asoul/tsec.git)

# Taiwan Stock Exchange Crawler

這是一個去爬 [台灣證券交易所](http://www.twse.com.tw/) 和 [證券櫃檯買賣中心](http://www.tpex.org.tw/) 的爬蟲，我修改了原作者起始日期，加入了挑選我要的股票的script，以及各股編號，並產生text.txt以寄到我的信箱。

## Setup

```
https://github.com/learningkeeper/tsec/tsec.git

$ cd tsec

$ pip install -r requirements.txt
```

## Usage

### Command

爬當日

```
$ python crawl.py
```

爬指定日期

```
$ python crawl.py YYYY MM DD

e.g.

$ python crawl.py 2016 02 15
```

### Flag

`-b, --back`: 往回爬直到 `2016/9/10`

`-c, --check`: 往回爬 10 天

### 後處理

清除重複的檔案，按日期排序

```
$ python post_process.py
```

## 資料格式

- 每個檔案的檔名 `XXX.csv`，`XXX` 是股票編號
- 每個檔案中有數列，每列為一天交易的資訊
- 每列包含：交易日期、成交股數、成交金額、開盤價、最高價、最低價、收盤價、漲跌價差、成交筆數，共 9 欄。
- 符號說明: +表示漲、- 表示跌、X表示不比價
- 當日統計資訊含一般、零股、盤後定價、鉅額交易，不含拍賣、標購。

範例：`104/02/13,7599922.0,528270219.0,69.35,69.65,69.35,69.45,0.45,1771.0`

## 資料來源

- [台灣證券交易所](http://www.twse.com.tw/)

- [證券櫃檯買賣中心](http://www.tpex.org.tw/)

## 附上免責聲明
僅供研究交流，
