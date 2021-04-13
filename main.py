# Loading Services
from dialogflow import DialogflowService

dialogflow = DialogflowService()

customer_info = {
    '100': {
        'name': "Amit",
        'address': "Mumbai"
    },
    '101': {
        'name': "Kunal",
        'address': "Chennai"
    },
    '102': {
        'name': "Babul",
        'address': "New delhi"
    },
    '103': {
        'name': "Vikas",
        'address': "Shimla"
    },
    '104': {
        'name': "Kripal",
        'address': "Gurgaon"
    },
    '105': {
        'name': "Chrish",
        'address': "New Delhi"
    },
    '106': {
        'name': "Anamika",
        'address': "Jaipur"
    },
    '107': {
        'name': "Ridhima",
        'address': "Newyork"
    },
    '108': {
        'name': "Kavitha",
        'address': "Bengaluru"
    },
    '109': {
        'name': "Harshit",
        'address': "Noida"
    },
    '110': {
        'name': "Piyush",
        'address': "Lucknow"
    },
    '111': {
        'name': "Akanksha",
        'address': "Pune"
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
            return f"Here is your customer info :- Name: {customer_info.get(customer_number).get('name')}, Address: {customer_info.get(customer_number).get('address')}"
        else:
            return "Customer info not present"

# bot = SalesBotPOC()
# while True:
#     print("Your Message -- ", end="")
#     message = input()
#     if message.lower() == 'stop':
#         print("Sales Bot -- Ok, Bye! See you soon")
#         break
#     else:
#         response, customer_number = bot.chatbot(message)
#         print(f"Sales Bot -- {response}")
#
#         if customer_number != "":
#             customer_number = customer_number.split(".")[0]
#             if customer_number in customer_info:
#                 print(f"Here is your customer info :- Name: {customer_info.get(customer_number).get('name')}, Address: {customer_info.get(customer_number).get('address')}")
#             else:
#                 print("Customer info not present")
