from flask import Flask, request
from main import SalesBotPOC
app = Flask(__name__)

bot = SalesBotPOC()

@app.route('/')
def home():
    return 'Welcome to Sales Bot POC!'


@app.route('/webhook/', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    fulfillmentText = ''
    query_result = req.get('queryResult')
    if query_result.get('action') == 'action.customer.information':
        customer_code = str(query_result.get('parameters').get('customer-number'))
        print(customer_code)
        fulfillmentText = bot.check_customer_detail(customer_code)
    return {
        "fulfillmentText": fulfillmentText,
        "source": "webhookdata"
    }


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
