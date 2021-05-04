from flask import Flask, request
from google.cloud import bigquery
from google.oauth2 import service_account

app = Flask(__name__)
credentials = service_account.Credentials.from_service_account_file('static/bigQueryCredential.json')

# variable
gcp_project = "dialogflow-311918"
bq_dataset = "sales_bot"

# connection
client = bigquery.Client(credentials=credentials, project=gcp_project)
# dataset_ref = client.dataset(bq_dataset)


def create_card_message():
    return {
        'cards': [{
            "header": {
                "title": "Do you want to look for customer information or sales revenue?"
            },
            "sections": [
                {
                    "widgets": [
                        {
                            "buttons": [
                                {
                                    "textButton": {
                                        "onClick": {
                                            "action": {
                                                "actionMethodName": "action.customer.information"
                                            }
                                        },
                                        "text": "Customer Information"
                                    }
                                },
                                {
                                    "textButton": {
                                        "onClick": {
                                            "action": {
                                                "actionMethodName": "action.sales.revenue"
                                            }
                                        },
                                        "text": "Sales Revenue"
                                    }
                                }
                            ]
                        }
                    ]
                }
            ]
        }]
    }


@app.route('/')
def home():
    return 'Welcome to Sales Bot POC!'


@app.route('/webhook/', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    query_result = req.get('queryResult')

    req2 = request.get_json()
    event = req2.get('originalDetectIntentRequest').get('payload').get('data').get('event')
    msg_type = event.get('type')
    user = event.get('user').get('displayName')
    print(f"type {msg_type} and user {user}****************************************************")
    fulfillment_text = ""
    if query_result.get('action') == 'input.welcome':
        create_card_message()
        fulfillment_text = f"Hello {user} to Imerys Sales Bot! How can I help you today?"


    elif query_result.get('action') == 'action.customer.information':
        customer_code = str(query_result.get('parameters').get('customer_number'))
        # Perform a query.
        query = f"SELECT Cust_Name, Cust_Address FROM `dialogflow-311918.sales_bot.cust_info` WHERE Cust_No = '{customer_code}'"
        query_job = client.query(query)  # API request
        rows = query_job.result()  # Waits for query to finish
        result = name = address = ""
        for row in rows:
            result = str(row)
            name = str(row.Cust_Name)
            address = str(row.Cust_Address)

        if result == "":
            fulfillment_text = 'Customer info not present'
        else:
            fulfillment_text = f"Customer information of {customer_code} is Name - {name} and Address - {address}"


    elif query_result.get('action') == 'action.sales.revenue':
        customer_code = str(query_result.get('parameters').get('customer_number'))
        sales_interval = str(query_result.get('parameters').get('sales_period'))

        # Perform a query.
        query = f"SELECT Cust_Name, Cust_Address, Sales_Amount FROM `dialogflow-311918.sales_bot.cust_info` WHERE Cust_No = '{customer_code}' and Month_Name = '{sales_interval}'"
        query_job = client.query(query)  # API request
        rows = query_job.result()  # Waits for query to finish
        result = name = address = sales_amount = ""
        for row in rows:
            result = str(row)
            name = str(row.Cust_Name)
            address = str(row.Cust_Address)
            sales_amount = str(row.Sales_Amount)

        if result == "":
            fulfillment_text = 'Customer info not present'
        else:
            fulfillment_text = f"Sales revenue for {customer_code} is Name - {name}, Address - {address} and Sales Amount - {sales_amount}"
    return {
        "fulfillmentText": fulfillment_text,
        "source": "webhookdata"
    }

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
