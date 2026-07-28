from langchain_core.tools import tool
from atlas_rt.stubs.databases import VISA_RULES_DB, PLACES_DB, FLIGHTS_DB, HOTELS_DB, ITINERARY_TEMPLATES, EMAIL_LOG, USER_DB, PAYMENT_LOG
from atlas_rt.stubs.aliases import Mapping
from datetime import datetime

@tool
def search_hotels(country: str) -> str:
  """This tool searches for hotels in the destination country"""
  key = country.lower().strip()
  hotels = HOTELS_DB.get(key, f"The hotel information is not available for the destination {country}.")
  return hotels

@tool 
def plan_itinerary(country: str) -> str:
  """This tool plans itinerary for the destination country"""
  key = country.lower().strip()
  itinerary = ITINERARY_TEMPLATES.get(key, f"There is no information available for the destination {country}")
  return itinerary


@tool
def send_email(to: str, subject: str, body: str) -> str:
  """Send an email with the itinerary or trip details to a recipient."""
  EMAIL_LOG.append({"to": to, "subject": subject, "body": body})
  return f"Email sent to {to}."

@tool
def get_visa_rules(country: str) -> str:
  """This tool searches for visa rules of the destination country"""
  key = country.lower().strip()
  visa_rules = VISA_RULES_DB.get(key,f"There are no visa rules available for this {country}.")
  return visa_rules

@tool
def search_places(country: str) -> str:
  """This tool searches for places to visit in the destination country"""
  key = country.lower().strip()
  places = PLACES_DB.get(key, f"There are no recommended places for this {country}.")
  return places


@tool
def look_up_user(user_id: str) -> str:
  """This tool fetches the currently logged in user's data using the provided user_id and loads it."""
  user_info = USER_DB.get(user_id)
  if user_info is None:
    return f"User ID {user_id} not found"
  return f"User Loaded: {user_info['name']} ({user_info['email']}) home airport {user_info['home_airport']} passport {user_info['passport_country']}"

@tool
def search_flights(origin: str, destination: str, start_date: str, end_date: str) -> str:
  """This tool searches for flights from the origin to destination and returns roundtrip flights for the start and end dates.
  If the dates are ambigious, assume them as dates for current year."""

  origin_code = Mapping.get(origin.lower().strip(), origin.strip()).upper()
  dest_code = Mapping.get(destination.lower().strip(), destination.strip()).upper()
  key = (origin_code, dest_code)
  flights = FLIGHTS_DB.get(key, f"There are no flights in the website from {origin} to {destination}.")
  return f"{flights} Travel dates: {start_date} to {end_date}"


@tool
def process_payment(user_id: str, amount: float, recipient: str) -> str:
    """
    This tool uses the payment information present in the user's information.
    Args:
        user_id: The current logged in user's user_id
        amount: Total sum of flights and hotels in US Dollars.
        recipient: The person recieving the payment, ex: The hotel's name.
        """
    timestamp = datetime.now().isoformat()
    user_info = USER_DB.get(user_id)
    if user_info is None:
        return "Sorry, There is no payment information on file"
    else:
        payment_info = user_info['payment_method']
        last_4 = payment_info['number'][-4:]
        PAYMENT_LOG.append({"user_id": user_id, "amount": amount, "recipient": recipient, "last_4": last_4, "timestamp": timestamp})
        return f"Payment processed. Card ending in {last_4}."
        

tools = [look_up_user, get_visa_rules, search_places, search_flights, search_hotels, plan_itinerary, send_email, process_payment]