from flask import Flask, request
from SQLServerConn import cursor

app = Flask(__name__)


@app.route('/')
def home():
    return 'Welcome to Sales Bot POC!'


@app.route('/webhook/', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    fulfillmentText = 'Customer info not present'
    query_result = req.get('queryResult')
    if query_result.get('action') == 'action.customer.information':
        customer_code = str(query_result.get('parameters').get('customer-number'))
        print(customer_code)
        cursor.execute(f'SELECT * FROM CustomerInfo_Dialogflow where CustomerCode = {customer_code}')
        row = cursor.fetchone()
        if row:
            fulfillmentText = row
    return {
        "fulfillmentText": fulfillmentText,
        "source": "webhookdata"
    }


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
