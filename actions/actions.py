# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []

class ActionJobSetup(Action):

    def name(self) -> Text:
        return "action_job_setup"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        intent = tracker.latest_message['intent'].get('name')
        last_message = tracker.latest_message['text'].lower()

        if "create" in last_message or "setup" in last_message or "configure" in last_message:
            dispatcher.utter_message(text="This is how you create a new job.")
        elif "cancel" in last_message:
            dispatcher.utter_message(text="To cancel a job, follow these steps.")
        elif "reschedule" in last_message:
            dispatcher.utter_message(text="Here is how you can reschedule a job.")
        elif "opt-out" in last_message or "opt out" in last_message:
            dispatcher.utter_message(text="To opt-out from a job, do this.")
        elif "status" in last_message:
            dispatcher.utter_message(text="The current status of your job is as follows.")
        elif "details" in last_message or "information" in last_message:
            dispatcher.utter_message(text="Here are the details of the job.")
        
        # Common response for grouped intents
        dispatcher.utter_message(text="This is a common response for job-related queries.")

        return []