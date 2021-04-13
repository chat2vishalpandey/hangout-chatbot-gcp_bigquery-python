import os
import uuid

import dialogflow_v2
from google.api_core.exceptions import InvalidArgument

import credential as cred

credentials_file = os.path.expanduser('dialogflow_auth_credential.json')
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_file

context_short_name = 'buddy_context_2'
context_name = "projects/" + cred.GOOGLE_PROJECT_ID + "/agent/sessions/" + cred.SESSION_ID + "/contexts/" + context_short_name.lower()
context = dialogflow_v2.types.context_pb2.Context(name=context_name)

session_client = dialogflow_v2.SessionsClient()
session = session_client.session_path(cred.GOOGLE_PROJECT_ID, str(uuid.uuid4()))


class DialogflowService():
    def __int__(self):
        self.msg = 'Dialogflow service is working'

    def send_text_query_to_dialogFlow(self, text_to_be_analyzed, params={}):
        # print('Session path: {}\n'.format(session))
        text_input = dialogflow_v2.types.TextInput(text=text_to_be_analyzed, language_code=cred.DF_LANGUAGE_CODE)
        query_input = dialogflow_v2.types.QueryInput(text=text_input)
        query_parameter = dialogflow_v2.types.QueryParameters(contexts=[context])

        try:
            response = session_client.detect_intent(session=session, query_input=query_input,
                                                    query_params=query_parameter)
        except InvalidArgument:
            raise
        text, customer_number = self.handle_dialogflow_action(response)
        return text, customer_number

    def send_event_to_dialogFlow(self, event_to_be_analyzed, params={}):
        event_input = dialogflow_v2.types.EventInput(name=event_to_be_analyzed, language_code=cred.DF_LANGUAGE_CODE)
        query_input = dialogflow_v2.types.QueryInput(event=event_input)
        query_parameter = dialogflow_v2.types.QueryParameters(contexts=[context])

        try:
            response = session_client.detect_intent(session=session, query_input=query_input,
                                                    query_params=query_parameter)
        except InvalidArgument:
            raise

        text = self.handle_dialogflow_action(response)
        return text

    def handle_dialogflow_action(self, response):
        action = response.query_result.action
        customer_number = ""
        if action == "action.customer.information":
            parameter = response.query_result.parameters.fields
            customer_number = str(dict(parameter).get('customer-number')).split(":")[1].strip().replace("\"","")
        text = response.query_result.fulfillment_text

        return text, customer_number
