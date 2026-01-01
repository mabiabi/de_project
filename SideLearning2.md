# Mastering Pandas "Method Chaining"

When you need to write code like this from scratch, ask yourself these four questions:
1. "What are my categories?" $\rightarrow$ This goes in `.groupby()`
2. "What numbers am I measuring?" $\rightarrow$ This goes in the brackets `['ColumnName']`
3. "What math do I need?" $\rightarrow$ This is your function like `.sum()` or `.mean()`
4. "How should I present it?" $\rightarrow$ This is where you add `.sort_values()` or `.head()`

Pro-Tip: Use Parentheses for Readability

When chains get long, they become hard to read.
You can wrap the whole expression in parentheses to break it into multiple lines:
```python

DataFrame.groupby('Country')['Quantity'].sum().sort_values(ascending=False)

# what follows is identical to above code but much easier to read

top_countries = (
    myDataFrame.groupby('Country')['Quantity']
    .sum()
    .sort_values(ascending=False)
)
```
```python
# it also equal to that comes before
myDataFrame.groupby('Country').Quantity.sum().sort_values(ascending=False)
# the Quantity column is called using dot notation like an attribute (not method) instead of brackets.

```

## How to understand the sequence
Think of it as a conversation where you narrow down your request step-by-step:

1. `df`: "Look at the whole table..."

2. `.groupby('Country')`: "...now, organize all those rows into piles based on their 'Country'."

3. `['Quantity']`: "...out of all the data in those piles, I only care about the 'Quantity' numbers."

4. `.sum()`: "...finally, add those numbers up for each pile."

Why it matters: If you left out the `['Quantity']` and just wrote `df.groupby('Country').sum()`, Pandas would try to sum every numeric column in your table (like Price, ID, or Tax) for every country. The brackets help you stay efficient by only calculating exactly what you need.

* In Python, parentheses `()` are used to call a function or method.

* In Pandas, square brackets `[]` are used for indexing or selecting specific data.

---
When you run df.groupby('Country'), you aren't actually calculating anything yet. You have created a DataFrameGroupBy object, which is essentially a "Plan of Action" or a blueprint stored in memory.

Pandas is being "lazy" (in a good way). It has organized the data into internal buckets but is waiting for you to tell it what math to do (sum, mean, etc.) before it actually performs the work.

`print(myDataFrame.groupby('Country').groups)` will show you how Pandas has internally grouped the rows by country, but no calculations have been done yet.

`print(myDataFrame.groupby('Country').get_group('Canada'))` See only the data for 'Canada'

```python
for name, group_df in myDataFrame.groupby('Country'):
    print(f"Group: {name}")
    print(group_df)
```
Iterate through it, You can loop through the object to see how Pandas has split the data. This is the 'mini-table' for that country.

the GroupBy object represents the **Split** stage. It is holding the data in separate "buckets" behind the scenes. It doesn't become a "normal" DataFrame again until you Apply a function (like `.sum()`) and Combine the results.

# How to understand any Python object
If you ever encounter a mysterious object like `<pandas.core.groupby...>` and want to know what it can do, use these three built-in Python tools:

- `type(obj)`: Tells you exactly what the object is.

       - Example: `type(my_group_object)`

- `dir(obj)`: Lists every single "button" (method) and "label" (attribute) available on that object.

       - Note: You'll see things like sum, mean, count, and apply in this list for a GroupBy object.

- `help(obj)`: Opens the manual. It provides a detailed description of what the object is for and how to use its methods.

## Using `agg()` function for multiple aggregation
```python
myDataFrame.groupby('Country').Quantity.agg(['sum', 'mean', 'std'])

>>>
                          sum       mean         std
Country                                             
Australia               83653  66.444003   97.686932
Austria                  4827  12.037406   21.745485
Bahrain                   260  13.684211   30.016759
Belgium                 23152  11.189947   13.601441
Brazil                    356  11.125000    8.476723
Canada                   2763  18.298013   46.682587
Channel Islands          9479  12.505277   22.570877
Cyprus                   6317  10.155949   23.263590
Czech Republic            592  19.733333   22.813990
Denmark                  8188  21.048843   27.402502
EIRE                   142637  17.403245   40.368435
European Community        497   8.147541    6.546847
Finland                 10666  15.346763   21.001421
France                 110480  12.911067   21.425031
Germany                117448  12.369458   17.865719
Greece                   1556  10.657534    7.724067
Hong Kong                4769  16.559028   16.936343
Iceland                  2458  13.505495   18.856172
Israel                   4353  14.656566   16.026474
Italy                    7999   9.961395   13.579809
Japan                   25218  70.441341  177.191079
Lebanon                   386   8.577778    4.314294
Lithuania                 652  18.628571   10.137542
Malta                     944   7.433071    8.069726
Netherlands            200128  84.406580  111.369151
Norway                  19247  17.722836   22.644876
Poland                   3653  10.712610   10.174628
Portugal                16180  10.651745   11.823938
RSA                       352   6.068966    3.329096
Saudi Arabia               75   7.500000    5.720334
Singapore                5234  22.855895   27.742886
Spain                   26824  10.589814   24.130396
Sweden                  35637  77.136364  128.891540
Switzerland             30325  15.147353   18.956901
USA                      1034   3.553265   16.450545
United Arab Emirates      982  14.441176   12.474909
United Kingdom        4263829   8.605486  227.588756
Unspecified              3300   7.399103    8.765735
```