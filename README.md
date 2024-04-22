# Enhanced Crypto Market-Making Algorithm with Stop Condition

### Overview
This repository contains an advanced crypto market-making trading algorithm that focuses on the "IOTA/BTC" trading pair on the Binance exchange. The algorithm is designed to leverage market-making strategies to profit from bid-ask spreads while effectively managing risks arising from price fluctuations and inventory changes.


![Flow Chart](https://github.com/vishnugovind10/MarketMaking/blob/main/Logic%20MM.jpg)


### Algorithm Highlights
- Dynamic Initial Balance Calculation: The algorithm queries exchange APIs to determine the initial account balance, forming a reliable baseline for P&L calculations.
- Advanced Order Book Analysis: Accurate market-making decisions are informed by in-depth order book analysis, optimizing bid and ask prices for optimal trade execution.
- Real-time P&L Monitoring: Trades are executed dynamically, with the algorithm consistently updating the Profit and Loss (P&L) value after each trade.
- Stop Condition Implementation: A stop condition mechanism is embedded to mitigate risk. If the current P&L falls below a predefined percentage of the initial balance, the algorithm halts trading operations.

### Instructions for Use
1. Replace API endpoints and keys in the code with actual credentials for Binance and Kraken exchanges.
2. Incorporate the code into your trading infrastructure, ensuring thorough testing in a controlled environment before deploying it for live trading.
3. Utilize the provided CSV output to monitor trading positions, P&L performance, and adherence to the stop condition.

### Important Notes
- Use this code responsibly and after thorough testing.
- The integrated stop condition feature provides a safeguard against significant losses, enhancing the algorithm's viability for successful crypto market-making endeavors.

### External Link
If you are interested in learning more about Market Making, refer to my medium article: https://vishnugovind10.medium.com/unveiling-the-world-of-decentralized-finance-defi-and-decentralized-exchanges-dexes-2e180a440e52
