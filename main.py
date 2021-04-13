# Loading Services
from dialogflow import DialogflowService

dialogflow = DialogflowService()

customer_info = {
    '100': {
        'name': "Amit",
        'address': "ABC"
    },
    '101': {
        'name': "Kunal",
        'address': "DFR"
    },
    '102': {
        'name': "Babul",
        'address': "GTR"
    },
    '103': {
        'name': "Vikas",
        'address': "SDT"
    },
}


class SalesBotPOC():

    def __int__(self):
        self.msg = 'Dialogflow service is working'

    def chatbot(self, message):
        response, customer_number = dialogflow.send_text_query_to_dialogFlow(message)
        return response, customer_number

    def check_customer_detail(self, customer_code):
        customer_number = customer_code.split(".")[0]
        if customer_number in customer_info:
            return "Here is your customer info :-"
        else:
            return "Customer info not present"


bot = SalesBotPOC()
while True:
    print("Your Message -- ", end="")
    message = input()
    if message.lower() == 'stop':
        print("Sales Bot -- Ok, Bye! See you soon")
        break
    else:
        response, customer_number = bot.chatbot(message)
        print(f"Sales Bot -- {response}")

        if customer_number != "":
            customer_number = customer_number.split(".")[0]
            if customer_number in customer_info:
                print("Here is your customer info :-")
            else:
                print("Customer info not present")
