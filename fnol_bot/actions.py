# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
#
#
class FaqForm(FormAction):

	def name(self) -> Text:
		"""Unique identifier of the form"""
		return "faq_form"

	@staticmethod
	def required_slots(tracker: Tracker) -> List[Text]:
		"""A list of required slots that the form has to fill"""

		return ["policy", "last_name", "unique_id", "dob", "zip_code"]

	def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
		"""A dictionary to map required slots to
		- an extracted entity
		- intent: value pairs
		- a whole message
		or a list of them, where a first match will be picked"""
		return {
		"policy": self.from_entity(entity="policy", intent="inform", not_intent=["chitchat"]),

		"last_name": self.from_entity(entity="last_name", intent="inform", not_intent=["chitchat", "request_faq"]),
		
		"unique_id": self.from_entity(entity="unique_id", intent="inform", not_intent=["chitchat", "request_faq"]),

		"zip_code": self.from_entity(entity="zip_code", intent="inform", not_intent=["chitchat", "request_faq"]),
				}
	
	def policy_db() -> List[Text]:
		"""Database of supported cuisines"""

		return ["POL3321096489", "POL3321849059", "POL3319046784", "POL3321849062"]

	def last_name_db() -> List[Text]:
		"""Database of supported cuisines"""

		return ["Smith", "Garcia", "Turner", "Richardson"]

	def unique_id_db() -> List[Text]:
		"""Database of supported cuisines"""

		return ["15476529", "35427329", "72402473", "73209423"]

	def dob_db() -> List[Text]:
		"""Database of supported cuisines"""

		return ["22/03/1996", "20/03/1995", "21/04/1994", "20/07/1992"]

	def zip_db() -> List[Text]:
		"""Database of supported cuisines"""

		return ["99501", "85001","72201","94203"]

	def validate_policy(
	self,
	value: Text,
	dispatcher: CollectingDispatcher,
	tracker: Tracker,
	domain: Dict[Text, Any],
	) -> Dict[Text, Any]:
		"""Validate cuisine value."""

		if value.lower() in self.policy_db():
		# validation succeeded, set the value of the "cuisine" slot to value
			return {"policy": value}
		else:
			dispatcher.utter_message(template="utter_wrong_policy")
		# validation failed, set this slot to None, meaning the
		# user will be asked for the slot again
			return {"policy": None}

	def validate_last_name(
	self,
	value: Text,
	dispatcher: CollectingDispatcher,
	tracker: Tracker,
	domain: Dict[Text, Any],
	) -> Dict[Text, Any]:
		"""Validate cuisine value."""

		if value.lower() in self.last_name_db():
			# validation succeeded, set the value of the "cuisine" slot to value
			return {"last_name": value}
		else:
			dispatcher.utter_message(template="utter_wrong_last_name")
		# validation failed, set this slot to None, meaning the
		# user will be asked for the slot again
			return {"last_name": None}

	def validate_unique_id(
	self,
	value: Text,
	dispatcher: CollectingDispatcher,
	tracker: Tracker,
	domain: Dict[Text, Any],
	) -> Dict[Text, Any]:
		"""Validate cuisine value."""

		if value.lower() in self.unique_id_db():
			# validation succeeded, set the value of the "cuisine" slot to value
			return {"unique_id": value}
		else:
			dispatcher.utter_message(template="utter_wrong_unique_id")
			# validation failed, set this slot to None, meaning the
			# user will be asked for the slot again
			return {"unique_id": None}

	def validate_zip_code(
	self,
	value: Text,
	dispatcher: CollectingDispatcher,
	tracker: Tracker,
	domain: Dict[Text, Any],
	) -> Dict[Text, Any]:
		"""Validate cuisine value."""

		if value.lower() in self.zip_db():
			# validation succeeded, set the value of the "cuisine" slot to value
			return {"zip_code": value}
		else:
			dispatcher.utter_message(template="utter_wrong_zip_code")
			# validation failed, set this slot to None, meaning the
			# user will be asked for the slot again
			return {"zip_code": None}

	def validate_dob(
	self,
	value: Text,
	dispatcher: CollectingDispatcher,
	tracker: Tracker,
	domain: Dict[Text, Any],
	) -> Dict[Text, Any]:
		"""Validate cuisine value."""

		if value.lower() in self.dob_db():
			# validation succeeded, set the value of the "cuisine" slot to value
			return {"dob": value}
		else:
			dispatcher.utter_message(template="utter_wrong_dob")
			# validation failed, set this slot to None, meaning the
			# user will be asked for the slot again
			return {"dob": None}

	def submit(
	self,
	dispatcher: CollectingDispatcher,
	tracker: Tracker,
	domain: Dict[Text, Any],
	) -> List[Dict]:
		"""Define what the form has to do
		after all required slots are filled"""

		# utter submit template
		dispatcher.utter_message(template="utter_submit")
		return []
