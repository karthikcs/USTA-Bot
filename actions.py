from rasa_core.actions import Action
from rasa_core.events import SlotSet
from rasa_core.events import UserUttered
from rasa_core.actions.forms import EntityFormField, FormAction


## Action to clear all the slots for the next conversation
class ActionClearSlots(Action):
    def name(self):
        return 'action_clear_slots'

    def run(self, dispatcher, tracker, domain):
        # dispatcher.utter_message("looking for restaurants")
        # restaurants = restaurant_api.search(tracker.get_slot("cuisine"))
        
        return [SlotSet("GPE", None), SlotSet("skill", None)]

## Check if madatory slots are empty and seek information
class ActionCheckSlots1(Action):
    def name(self):
        return 'action_check_slots1'

    def run(self, dispatcher, tracker, domain):
        # dispatcher.utter_message("looking for restaurants")
        # restaurants = restaurant_api.search(tracker.get_slot("cuisine"))
        waiting = None
        for k, v in tracker.current_slot_values().items():
            if(v == None ):
                dispatcher.utter_message("Looking value for " + k )
                waiting = "Y"
                # UtterAction("action_listen")
        if(waiting == None ):
            print("Inside")
            intent = {"name": "search_candidate_final", "confidence": 1.0}
            print(tracker.update(UserUttered("/search_candidate_final", intent, [])))
            print(tracker.events)
            return [UserUttered("/search_candidate_final", intent, [])]
            # UtterAction("action_restart")
        return []

class ActionCheckSlots(FormAction):
    def name(self):
        return 'action_check_slots'

    @staticmethod
    def required_fields():
        return [EntityFormField("GPE", "GPE"),
            EntityFormField("skill", "skill"),
        ]
    
    def submit(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Looking value for people with skill " + tracker.get_slot("skill") + 
         " in and around " + tracker.get_slot("GPE"))

class action_check_slots2(FormAction):
    def name(self):
        return 'action_check_slots2'

    @staticmethod
    def required_fields():
        return [EntityFormField("GPE", "GPE"),
            EntityFormField("skill", "skill"),
        ]
    
    def submit(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Looking value for people with skill " + tracker.get_slot("skill") + 
         " in and around " + tracker.get_slot("GPE"))
        from rasa_core.events import Restarted

        dispatcher.utter_template("utter_restart", tracker,
                                  silent_fail=True)
        return [Restarted()]
        
class ActionCreateHL(Action):
    def name(self):
        return 'action_hotlist_create'
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("API Called with hotlist name " + tracker.get_slot("hotlist"))
    
    