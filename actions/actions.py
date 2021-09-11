from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk import Action


import smtplib
from email.mime.text import MIMEText

smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
smtp_ssl_port = 465
username = 'buildfast1011'
password = 'Ankit@1011'
sender = 'buildfast1011@gmail.COM'


class BuyHomeForm(FormAction):
    def name(self):
        return "buy_form"

    def required_slots(self,tracker) -> List[Text]:
        return ["country","cost","bedrooms","bathrooms","months","property_type","email"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
                "country": [
                    self.from_text(),
                ],
                "cost": [
                    self.from_text(),
                ],                
                "bedrooms": [
                    self.from_text(),
                ],
                "bathrooms": [
                    self.from_text(),
                ],
                "months": [
                    self.from_text(),
                ],
                "property_type": [
                    self.from_text(),
                ],
                "email": [
                    self.from_text(),
                ],
            }
    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
        ) -> List[Dict]:
        print(tracker.current_slot_values())
        email = tracker.get_slot("email")
        targets = [email]
        msg = MIMEText('Hi, how are you today?')
        msg['Subject'] = 'Hello'
        msg['From'] = sender
        msg['To'] = ', '.join(targets)

        server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
        server.login(username, password)
        server.sendmail(sender, targets, msg.as_string())
        server.quit()

        
        dispatcher.utter_message(template="utter_submit")
        # dispatcher.utter_template("utter_submit_buy", tracker)    
        return []

class sellHomeForm(FormAction):
    def name(self):
        return "sell_form"

    def required_slots(self,tracker) -> List[Text]:
        return ["time_to_sell","address","city","zipcode","email","phone_number"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
                "time_to_sell": [
                    self.from_text(),
                ],
                "address": [
                    self.from_text(),
                ],
                
                "city": [
                    self.from_text(),
                ],
                "zipcode": [
                    self.from_text(),
                ],
                "email": [
                    self.from_text(),
                ],
                "phone_number": [
                    self.from_text(),
                ],
            }
    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
        ) -> List[Dict]:
        dispatcher.utter_template("utter_submit_buy", tracker)    
        return []