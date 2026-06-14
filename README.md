# Binance Futures Demo Trading Bot

## Overview

A Python CLI application for placing Market and Limit orders on Binance Futures Demo Trading environment.

## Features

* Market Orders
* Limit Orders
* BUY and SELL support
* CLI-based input
* Input validation
* Logging
* Exception handling

## Installation

```bash
pip install -r requirements.txt
```

## Configure

Create a `.env` file:

```env
API_KEY=your_api_key
API_SECRET=your_api_secret
```

## Run Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

## Run Limit Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
├── cli.py
├── README.md
├── requirements.txt
└── .env
```

## Note

Binance Demo Futures endpoint was used:

[https://demo-fapi.binance.com](https://demo.binance.com/en/my/orders/futures/openorder)

This is Binance's current Futures Demo Trading environment.
