# Trading-bot - #1 Quant Trading & Technical Analysis Bot - 4,100+ stars & 1,000+ forks (https://github.com/AngryX-27/Trading-bot.git)

Trading-bot is a command line tool that automates cryptocurrency Technical Analysis (TA). It's maintained by a community of traders, engineers, data scientists, project managers, and many generous individuals dedicated to democratizing equal and open access to Bitcoin — the greatest wealth redistribution experiment in human history and monetary policy.

## Monitor over 500 cryptocurrencies across Bittrex, Binance, Bittrex, Bitfinex, Coinbase, Gemini and additional exchanges!

(Subject to regional financial regulations governing your jurisdiction and financial activities. Marketing or enabling does not constitute approval or endorsement of any activity - financial or otherwise. All risks are assumed and borne by you. Exercise caution & make prudent decisions.)

## Technical Analysis Automated:

- Momentum
- Relative Strength Index (RSI)
- Ichimoku Cloud (Leading Span A, Leading Span B, Conversion Line, Base Line)
- Simple Moving Average
- Exponential Moving Average
- MACD
- MFI
- OBV
- VWAP

## Alerts:

- SMS via Twilio
- Email
- Slack
- Telegram
- Discord

## Features:

- Modular code for easy trading strategy implementation
- Easy install with Docker

You can build on top of this tool and implement algorithm trading and some machine learning models to experiment with predictive analysis.

### Founded by Abenezer Mamo @ www.Mamo.io & www.linkedin.com/in/AbenezerMamo

## Installing And Running

The commands listed below are intended to be run in a terminal.

1. Install [docker CE](https://docs.docker.com/install/)

1. Create a config.yml file in your current directory. See the Configuring config.yml section below for customizing settings.

1. In a terminal run the application. `docker run --rm -v $PWD/config.yml:/app/config.yml shadowreaver/crypto-signal:master`.

1. When you want to update the application run `docker pull shadowreaver/crypto-signal:master`

### Configuring config.yml

For a list of all possible options for config.yml and some example configurations look [here](docs/config.md)

# FAQ

## Common Questions

### Why does Tradingview show me different information than crypto-signal?

There are several reasons why the information provided by crypto-signal might differ from tradingview, and truthfully, we cannot be 100% certain why these differences exist. Below are some factors affecting indicators that may vary between crypto-signal and tradingview.

- tradingview will have more historical data and for some indicators this can make a [big difference](https://ta-lib.org/d_api/ta_setunstableperiod.html).

- tradingview uses a rolling 15 minute timeframe which means that the data they are analyzing can be more recent than ours by a factor of minutes or hours depending on what candlestick timeframe you are using.

- tradingview may collect data in a way that means the timeperiods we have may not line up with theirs, which can have an effect on the analysis. This seems unlikely to us, but stranger things have happened.

### So if it doesn't match Tradingview how do you know your information is accurate?

The foundation of crypto-signal's technical analysis is TA-Lib, an open source technical analysis project that began in 1999. This library has been utilized in numerous technical analysis projects over the past two decades and remains one of the most trusted open source libraries for analyzing candlestick data.

# Liability

I am not your financial adviser, nor is this tool. Use this program as an educational resource, and nothing more. None of the contributors to this project are responsible for any losses you may incur. Be prudent and always conduct your own research.

We suggest you start by understanding the fundamental principles used in traditional asset classes as they exhibit lower volatility, and apply your knowledge through simulated trading before risking your aspirations.
