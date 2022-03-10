# **Market Making in Python**

This is a market neutral algorithm desdigned to provide liquidity for crypto tokens.

A simple market making algorithm which does the following:

1)   Providing quotes around a predictive fair value.

2)   Managing risk (inventory, adverse selection…)


The market data are in the below format:

1)  All order books over a period of time of a token in JSON

2)  All trades on that same market over the same period, in CSV

**Flow Chart of the Algorithm Logic**

![](MMFlow.jpeg)

