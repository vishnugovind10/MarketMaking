# **Market Making in Python**

This algorithm is a market neutral approach for providing liquidity for crypto tokens. It automates the process of providing quotes around a predictive fair value, by dynamically adjusting bid and ask values according to the market data. The algorithm also provides risk management by managing inventory, tracking order book and monitoring adverse selection.

The market data used in this algorithm is in JSON and CSV formats and comprises all order books over a period of time of a token, as well as all trades on that same market over the same period.

Using the Python code provided, the algorithm takes the market data and tracks the highest bid, lowest ask, fair value and spread percentage. 
If the spread percentage is less than the fees, the algorithm will not take any action. If, however, the spread percentage is greater than the fees, the algorithm will adjust the bid and ask values accordingly. The algorithm will also monitor the positions, and if the difference between the bid and ask values is greater than 10, it will adjust its positions accordingly.

Finally, the algorithm creates a CSV file of all its positions, which can be used to track its performance and adjust the algorithm as needed.


**Flow Chart of the Algorithm Logic**

![](MMFlow.jpeg)

