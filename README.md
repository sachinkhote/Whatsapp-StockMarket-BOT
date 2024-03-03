# Stock Market WhatsApp Bot

This project implements a WhatsApp bot that provides stock market information using the Twilio API and the MarketStack API.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- [Twilio](https://www.twilio.com/docs/sms/whatsapp/quickstart/python)
- [MarketStack API](https://marketstack.com/documentation)
- [ngrok](https://ngrok.com/)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sachinkhote/Whatsapp-StockMarket-BOT.git
```
```bash
cd stock-market-whatsapp-bot
```

2. Create and activate a virtual environment:
```bash
python3 -m venv myvenv
```
```bash
myvenv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Activate the Flask app:
```bash
set FLASK_APP=app.py
```

## Configuration

1. Set up your Twilio account and obtain your account ID and token.

2. Set the following environment variables:

   - `TWILIO_ACCOUNT`: Your Twilio account ID.
   - `TWILIO_TOKEN`: Your Twilio authentication token.
   - `MARKETSTACK_KEY`: Your MarketStack API key.

## Usage

1. Run ngrok to expose your local server:
```bash
ngrok http 5000
```

2. Set up a Twilio webhook for incoming WhatsApp messages. Use the ngrok URL followed by `/webhook` as the webhook URL.

3. Run the Flask app:
```bash
python app.py
```
4. Send messages to your WhatsApp bot to query stock prices. Start with "Hi" to get started.


## Contact

For questions or support, contact [sachinkhote451@gmail.com](mailto:sachinkhote451@gmail.com).
