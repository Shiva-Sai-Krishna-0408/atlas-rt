from langchain_core.tools import tool
from atlas_rt.stubs.databases import VISA_RULES_DB, PLACES_DB, FLIGHTS_DB, HOTELS_DB, ITINERARY_TEMPLATES, EMAIL_LOG

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
def search_flights(origin: str, destination: str, start_date: str, end_date: str) -> str:
  """This tool searches for flights from the origin to destination and returns roundtrip flights for the start and end dates"""

  key = (origin.lower().strip(),destination.lower().strip())
  flights = FLIGHTS_DB.get(key, f"There are no flights in the website from {origin} to {destination}.")
  return f"{flights} Travel dates: {start_date} to {end_date}"

tools = [get_visa_rules, search_places, search_flights, search_hotels, plan_itinerary, send_email]