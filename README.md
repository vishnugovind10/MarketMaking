# Comprehensive Crypto Market-Making Algorithm with Portfolio Rebalancing

**Introduction:**
This repository features an advanced Python script encompassing both a crypto market-making trading algorithm and a portfolio rebalancing mechanism. The algorithm aims to capitalize on the bid-ask spread in the cryptocurrency market, while the portfolio rebalancing strategy ensures consistent asset allocation. The trading algorithm focuses on the "IOTA/BTC" trading pair on the Binance exchange.

**Features:**
- **Market-Making Algorithm:** The algorithm utilizes real-time order book and trade data to make market-making decisions, aiming to profit from the bid-ask spread.
- **Portfolio Rebalancing:** A sophisticated portfolio rebalancing mechanism dynamically adjusts asset positions to maintain desired weights.
- **Risk Management:** The algorithm incorporates risk management techniques to safeguard against significant losses.
- **Adaptive Position Sizing:** Position sizes are dynamically adjusted based on market conditions and predefined rules.

## Implementation Sections:

1. **Initialization and Constants:**
   - Essential libraries are imported, including pandas for data manipulation and json for JSON data handling.
   - Binance API endpoints and keys are defined for data retrieval.
   - Initial account balance is fetched from the exchange to establish a baseline.

2. **Fetching Trade and Order Book Data:**
   - Trade data is fetched from the Binance API and stored in a DataFrame.
   - Order book data is obtained and processed into a DataFrame containing bid and ask prices.

3. **Calculating Fair Value and Spread Percentage:**
   - Fair value is calculated for each trade as the midpoint between the highest bid and lowest ask prices.
   - The spread percentage, representing the bid-ask spread relative to the ask price, is computed.

4. **Trading Decision and Position Management:**
   - Bid and ask prices are determined using fair value and spread information.
   - Trades are executed based on bid and ask prices, while managing trading positions using a "flag" variable.
   - The algorithm's direction (neutral, long, short) is adjusted based on trade outcomes for risk management.

5. **Portfolio Rebalancing Strategy:**
   - The algorithm incorporates a portfolio rebalancing mechanism that maintains desired asset weights.
   - Asset positions are dynamically adjusted if current weights deviate from predefined thresholds.

6. **Output and Position Tracking:**
   - Trading positions are tracked using separate lists for bid positions, ask positions, and trade prices.
   - Every 1000 trades, current positions are saved to a DataFrame named "positions" and exported to a CSV file.

7. **Final Position Tracking and Output:**
   - Once all trades are processed, a final positions DataFrame is created and exported to "positions.csv."
   - The CSV file captures the comprehensive trading positions and profit/loss calculations.

## Key Concepts:

1. **Fair Value:**
   - Fair value represents the theoretical price at which an asset should trade based on supply and demand.
   - In this algorithm, fair value is estimated as the midpoint between the highest bid and lowest ask prices.

2. **Risk Management and Inventory:**
   - Risk management is executed by adapting the trading strategy based on net positions.
   - If net positions become heavily imbalanced (more than 10 positions in one direction), the algorithm switches direction to mitigate risk.

3. **Adverse Selection Mitigation:**
   - Adverse selection risks, where transaction costs erode potential gains due to narrow spreads, are mitigated.
   - The algorithm avoids trading when the spread is too narrow, optimizing profitability.

**Usage:**
1. Replace `'your-api-key'` with your actual Binance API key.
2. Define or implement missing functions such as `get_top_crypto_pairs()`.
3. Set appropriate strategy parameters: `threshold`, `exchange_fee_rate`, `max_loss_percentage`.
4. Run the script and observe the combined market-making and rebalancing strategies in action.

**Conclusion:**
This Python script exemplifies a comprehensive approach to crypto trading by integrating market-making strategies with portfolio rebalancing. The algorithm provides insights into how automation, risk management, and adaptive position sizing can be harnessed to achieve consistent profitability while maintaining balanced portfolio allocations. Users can customize and further enhance this script to align with their unique trading objectives and risk tolerances.
