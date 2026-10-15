# Stock Portfolio Tracker

A simple console program that calculates the total value of a stock portfolio
using a hardcoded price dictionary, with optional saving to `.txt` or `.csv`.

## Features
- Hardcoded dictionary of stock prices (AAPL, TSLA, GOOGL, MSFT, AMZN)
- Input validation (unknown stocks, non-numeric or non-positive quantities)
- Formatted table with per-stock value and total investment
- Optional export to `portfolio.txt` or `portfolio.csv`

## Run
```
python stock_tracker.py
```
Requires Python 3.6+. No external libraries.

## Test
```
python -m unittest test_stock_tracker.py
```

## Sample session
```
Stock name (or 'done'): aapl
Quantity of AAPL: 10
Stock name (or 'done'): tsla
Quantity of TSLA: 5
Stock name (or 'done'): done

Stock    Qty       Price           Value
AAPL      10      180.00        1,800.00
TSLA       5      250.00        1,250.00
TOTAL INVESTMENT                3,050.00
```

## Concepts used
Dictionary, input/output, basic arithmetic, loops, functions, file handling (`open`, `csv`).
