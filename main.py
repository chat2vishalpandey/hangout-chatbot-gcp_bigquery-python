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


while True:

    print("Your Message -- ", end = "")
    message = input()
    if message.lower() == 'stop':
        print("Sales Bot -- Ok, Bye! See you soon")
        break
    else:
        response, customer_number = dialogflow.send_text_query_to_dialogFlow(message)
        print(f"Sales Bot -- {response}")
        if customer_number != "":
            customer_number = customer_number.split(".")[0]
            if customer_number in customer_info:
                print("Here is your customer info :-")
            else:
                print("Customer info not present")