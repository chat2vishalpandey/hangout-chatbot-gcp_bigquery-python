# Loading Services
from dialogflow import DialogflowService
from SQLServerConn import cursor

dialogflow = DialogflowService()


class SalesBotPOC:

    def __int__(self):
        self.msg = 'Dialogflow service is working'

    def chatbot(self, message):
        response, customer_number = dialogflow.send_text_query_to_dialogFlow(message)
        return response, customer_number

    def check_customer_detail(self, customer_code):
        customer_number = customer_code.split(".")[0]
        cursor.execute(f'SELECT * FROM CustomerInfo_Dialogflow where CustomerCode = {customer_number}')
        row = cursor.fetchone()
        if row:
            return row
        else:
            return 'Customer info not present'


bot = SalesBotPOC()
while True:
    print("Your Message -- ", end="")
    message = input()
    if message.lower() == 'stop':
        print("Sales Bot -- Ok, Bye! See you soon")
        break
    else:
        response, customer_number = bot.chatbot(message)

        if customer_number != "":
            res = bot.check_customer_detail(customer_number)
            print(f"Sales Bot -- Here is your result, {res}")
        else:
            print(f"Sales Bot -- {response}")
