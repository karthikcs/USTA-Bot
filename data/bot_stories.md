## Story 1
* greet              
  - utter_greet
  - utter_ask_howcanhelp
* search_candidate
  - action_check_slots
* inform{"GPE": "New York"}
  - action_check_slots
* inform{"skill": ".Net"}
  - utter_sure
* sure
  - action_check_slots
  - action_restart

## Story 2
* greet              
  - utter_greet
  - utter_ask_howcanhelp
* search_candidate
  - action_check_slots
* inform{"skill": ".Net"}
  - action_check_slots
* inform{"GPE": "New York"}
  - utter_sure
* sure  
  - action_check_slots  
  - action_restart

## Story 3
* greet              
  - utter_greet
  - utter_ask_howcanhelp
* search_candidate{"GPE": "New York", "skill": ".Net"}
  - utter_sure
* sure  
  - action_check_slots
  - action_restart

## Story 4
* greet              
  - utter_greet
  - utter_ask_howcanhelp
* search_candidate{"GPE": "New York"}
  - action_check_slots
* inform{"skill": ".Net"}
  - utter_sure
* sure  
  - action_check_slots  
  - action_restart

## Story 5
* greet              
  - utter_greet
  - utter_ask_howcanhelp
* search_candidate{"skill": ".Net"}
  - action_check_slots
* inform{"GPE": "India"}
  - utter_sure
* sure  
  - action_check_slots  
  - action_restart

## Story for creating hotlist
* greet              
  - utter_greet
  - utter_ask_howcanhelp
* create_hotlist
  - utter_ask_name
* inform{"hotlist": "list1"}
  - action_hotlist_create
  - utter_hotlist_created
  - action_restart

## Story for creating hotlist with name 
* greet              
  - utter_greet
  - utter_ask_howcanhelp
* create_hotlist{"hotlist": "list1"}
  - action_hotlist_create
  - utter_hotlist_created
  - action_restart

## Help Story
* help
  - utter_help
  - action_restart

## Fallback
- utter_default  