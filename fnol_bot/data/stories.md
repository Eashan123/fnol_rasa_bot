## happy path
* greet
    - utter_happy_path
    - utter_greet
* request_faq
    - utter_ask_policy
    - faq_form
    - form{"name": "faq_form"}
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## unhappy path
* greet
    - utter_unhappy_path
    - utter_greet
* request_faq
    - faq_form
    - form{"name": "faq_form"}
* chitchat
    - utter_chitchat
    - faq_form
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_noworries


## bot challenge
* bot_challenge
  - utter_bot_challenge
  - utter_iamabot

## interactive_story_1
* greet
    - utter_greet
* request_faq
    - utter_ask_policy
* inform{"policy": "POL1234567899"}
    - faq_form
    - utter_ask_policy
    - utter_ask_policy
* inform{"policy": "POL1234567899"}
    - utter_slots_values
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
