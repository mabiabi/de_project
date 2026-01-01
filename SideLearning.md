# Pandas 12 Most Used Functions
This document provides examples of 12 commonly used functions in the Pandas library for data manipulation and analysis. Each function is demonstrated with code snippets and sample outputs using a hypothetical DataFrame named `myDataFrame`.

## 0. Importing Pandas and Loading Data

```
import pandas as pd
import numpy as np

myDataFrame = pd.read_csv("to/your/file/path/file_name.csv")
```

## 1. Head and Tail
```
>>> myDataFrame.head()

>>>
  InvoiceNo StockCode                          Description  Quantity          InvoiceDate  UnitPrice  CustomerID         Country
0    536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER         6  2010-12-01 08:26:00       2.55     17850.0  United Kingdom
1    536365     71053                  WHITE METAL LANTERN         6  2010-12-01 08:26:00       3.39     17850.0  United Kingdom
2    536365    84406B       CREAM CUPID HEARTS COAT HANGER         8  2010-12-01 08:26:00       2.75     17850.0  United Kingdom
3    536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE         6  2010-12-01 08:26:00       3.39     17850.0  United Kingdom
4    536365    84029E       RED WOOLLY HOTTIE WHITE HEART.         6  2010-12-01 08:26:00       3.39     17850.0  United Kingdom

>>> myDataFrame.tail()

>>>
       InvoiceNo StockCode                      Description  Quantity          InvoiceDate  UnitPrice  CustomerID Country
541904    581587     22613      PACK OF 20 SPACEBOY NAPKINS        12  2011-12-09 12:50:00       0.85     12680.0  France
541905    581587     22899     CHILDREN'S APRON DOLLY GIRL          6  2011-12-09 12:50:00       2.10     12680.0  France
541906    581587     23254    CHILDRENS CUTLERY DOLLY GIRL          4  2011-12-09 12:50:00       4.15     12680.0  France
541907    581587     23255  CHILDRENS CUTLERY CIRCUS PARADE         4  2011-12-09 12:50:00       4.15     12680.0  France
541908    581587     22138    BAKING SET 9 PIECE RETROSPOT          3  2011-12-09 12:50:00       4.95     12680.0  France
```
## 2. DataFrame information

```
>>> myDataFrame.info()

>>>
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 541909 entries, 0 to 541908
Data columns (total 8 columns):
 #   Column       Non-Null Count   Dtype  
---  ------       --------------   -----  
 0   InvoiceNo    541909 non-null  object 
 1   StockCode    541909 non-null  object 
 2   Description  540455 non-null  object 
 3   Quantity     541909 non-null  int64  
 4   InvoiceDate  541909 non-null  object 
 5   UnitPrice    541909 non-null  float64
 6   CustomerID   406829 non-null  float64
 7   Country      541909 non-null  object 
dtypes: float64(2), int64(1), object(5)
memory usage: 33.1+ MB
```

## 3. Shape and Size

```
>>> myDataFrame.shape
>>>
(541909, 8)

>>> myDataFrame.size
>>>
4335272  #541909*8
```

## 4. Statistical Summary (discribe() method and it's transposed)

```
>>> myDataFrame.describe()
>>>
            Quantity      UnitPrice     CustomerID
count  541909.000000  541909.000000  406829.000000
mean        9.552250       4.611114   15287.690570
std       218.081158      96.759853    1713.600303
min    -80995.000000  -11062.060000   12346.000000
25%         1.000000       1.250000   13953.000000
50%         3.000000       2.080000   15152.000000
75%        10.000000       4.130000   16791.000000
max     80995.000000   38970.000000   18287.000000

>>> myDataFrame.describe(include='all').T
>>>
                count unique                                 top    freq         mean          std       min      25%      50%      75%      max
InvoiceNo      541909  25900                              573585    1114          NaN          NaN       NaN      NaN      NaN      NaN      NaN
StockCode      541909   4070                              85123A    2313          NaN          NaN       NaN      NaN      NaN      NaN      NaN
Description    540455   4223  WHITE HANGING HEART T-LIGHT HOLDER    2369          NaN          NaN       NaN      NaN      NaN      NaN      NaN
Quantity     541909.0    NaN                                 NaN     NaN      9.55225   218.081158  -80995.0      1.0      3.0     10.0  80995.0
InvoiceDate    541909  23260                 2011-10-31 14:41:00    1114          NaN          NaN       NaN      NaN      NaN      NaN      NaN
UnitPrice    541909.0    NaN                                 NaN     NaN     4.611114    96.759853 -11062.06     1.25     2.08     4.13  38970.0
CustomerID   406829.0    NaN                                 NaN     NaN  15287.69057  1713.600303   12346.0  13953.0  15152.0  16791.0  18287.0
Country        541909     38                      United Kingdom  495478          NaN          NaN       NaN      NaN      NaN      NaN      NaN
```
##  5. Sample rows

```
>>> myDataFrame.sample(5)
>>> 
       InvoiceNo StockCode                   Description  Quantity          InvoiceDate  UnitPrice  CustomerID         Country
491826    578074     23583      LUNCH BAG PAISLEY PARK           2  2011-11-22 16:06:00       1.65     17590.0  United Kingdom
60458     541422     21633  SUNFLOWER DECORATIVE PARASOL         1  2011-01-17 17:48:00       8.29         NaN  United Kingdom
437394    574290     23394    POSTE FRANCE CUSHION COVER         2  2011-11-03 15:18:00       3.75     17403.0  United Kingdom
256842    559506     22504   CABIN BAG VINTAGE RETROSPOT         1  2011-07-08 15:17:00      16.63         NaN  United Kingdom
467061    576339     22123          PING MICROWAVE APRON         3  2011-11-14 15:27:00       4.13     14096.0  United Kingdom
```

## 6. Checking for missing values
`myDataFrame.isnull()` will give you a dataframe that each cell contains True or False depending on whether the value is null or not.

then you can use `.sum()` to count the number of True values in each column.

```
>>> myDataFrame.isnull().sum()
>>>
InvoiceNo           0
StockCode           0
Description      1454
Quantity            0
InvoiceDate         0
UnitPrice           0
CustomerID     135080
Country             0
dtype: int64
```
## 7. Unique entries

```
>>> myDataFrame.nunique()
>>>
InvoiceNo      25900
StockCode       4070
Description     4223
Quantity         722
InvoiceDate    23260
UnitPrice       1630
CustomerID      4372
Country           38
dtype: int64
```
## 8. Checking for duplicates
`myDataFrame.duplicated()` will return a Boolean Series where each entry indicates whether that row is a duplicate of a previous row.

When you call `.sum()` on a Boolean Series, it adds up all the True values. Therefore, the result is the total number of duplicate rows in your dataset.

```
>>> myDataFrame.duplicated().sum()
>>>
np.int64(5268) #number of duplicate rows
```
## 9. Value Counts
this function is used to get a count of unique values in a column. It returns a Series containing counts of unique values.

```
>>> myDataFrame['Country'].value_counts()
>>>

Country
United Kingdom          495478
Germany                   9495
France                    8557
EIRE                      8196
Spain                     2533
Netherlands               2371
Belgium                   2069
Switzerland               2002
Portugal                  1519
Australia                 1259
Norway                    1086
Italy                      803
Channel Islands            758
Finland                    695
Cyprus                     622
Sweden                     462
Unspecified                446
Austria                    401
Denmark                    389
Japan                      358
Poland                     341
Israel                     297
USA                        291
Hong Kong                  288
Singapore                  229
Iceland                    182
Canada                     151
Greece                     146
Malta                      127
United Arab Emirates        68
European Community          61
RSA                         58
Lebanon                     45
Lithuania                   35
Brazil                      32
Czech Republic              30
Bahrain                     19
Saudi Arabia                10
Name: count, dtype: int64
```
## 10. Sorting values
this function is used to sort the DataFrame by the values of one or more columns.

```
>>> myDataFrame.sort_values(by='Quantity', ascending=False).head()
>>> 
       InvoiceNo StockCode                        Description  Quantity          InvoiceDate  UnitPrice  CustomerID         Country
540421    581483     23843        PAPER CRAFT , LITTLE BIRDIE     80995  2011-12-09 09:15:00       2.08     16446.0  United Kingdom
61619     541431     23166     MEDIUM CERAMIC TOP STORAGE JAR     74215  2011-01-18 10:01:00       1.04     12346.0  United Kingdom
502122    578841     84826     ASSTD DESIGN 3D PAPER STICKERS     12540  2011-11-25 15:57:00       0.00     13256.0  United Kingdom
74614     542504     37413                                NaN      5568  2011-01-28 12:03:00       0.00         NaN  United Kingdom
421632    573008     84077  WORLD WAR 2 GLIDERS ASSTD DESIGNS      4800  2011-10-27 12:26:00       0.21     12901.0  United Kingdom
```
## 11. Grouping data
this function is used to group the DataFrame by the values of one or more columns and perform aggregate functions on the grouped data.

```
>>> myDataFrame.groupby('Country')['Quantity'].sum().sort_values(ascending=False)
>>>
 
Country
United Kingdom          4263829
Netherlands              200128
EIRE                     142637
Germany                  117448
France                   110480
Australia                 83653
Sweden                    35637
Switzerland               30325
Spain                     26824
Japan                     25218
Belgium                   23152
Norway                    19247
Portugal                  16180
Finland                   10666
Channel Islands            9479
Denmark                    8188
Italy                      7999
Cyprus                     6317
Singapore                  5234
Austria                    4827
Hong Kong                  4769
Israel                     4353
Poland                     3653
Unspecified                3300
Canada                     2763
Iceland                    2458
Greece                     1556
USA                        1034
United Arab Emirates        982
Malta                       944
Lithuania                   652
Czech Republic              592
European Community          497
Lebanon                     386
Brazil                      356
RSA                         352
Bahrain                     260
Saudi Arabia                 75
Name: Quantity, dtype: int64
```
## 12. Creating a new column
you can create a new column in the DataFrame by assigning a Series or a list to a new column name (TotalPrice).

```
>>> myDataFrame['TotalPrice'] = myDataFrame['Quantity'] * myDataFrame['UnitPrice']
>>> myDataFrame.head()

>>>
 
  InvoiceNo StockCode                          Description  Quantity          InvoiceDate  UnitPrice  CustomerID         Country  TotalPrice
0    536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER         6  2010-12-01 08:26:00       2.55     17850.0  United Kingdom       15.30
1    536365     71053                  WHITE METAL LANTERN         6  2010-12-01 08:26:00       3.39     17850.0  United Kingdom       20.34
2    536365    84406B       CREAM CUPID HEARTS COAT HANGER         8  2010-12-01 08:26:00       2.75     17850.0  United Kingdom       22.00
3    536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE         6  2010-12-01 08:26:00       3.39     17850.0  United Kingdom       20.34
4    536365    84029E       RED WOOLLY HOTTIE WHITE HEART.         6  2010-12-01 08:26:00       3.39     17850.0  United Kingdom       20.34
```
