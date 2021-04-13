from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def home():
    return 'Welcome to Sales Bot POC!'


@app.route('/webhook/', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    fulfillmentText = ''
    sum = 0
    query_result = req.get('queryResult')
    if query_result.get('action') == 'action.customer.information':
        customer_code = str(query_result.get('parameters').get('customer-number'))
        print(customer_code)
        fulfillmentText = f"You have provide customer code {customer_code}"
    return {
        "fulfillmentText": fulfillmentText,
        "source": "webhookdata"
    }


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
