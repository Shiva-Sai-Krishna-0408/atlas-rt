VISA_RULES_DB = {
    "japan": "Tourist visa-free for 90 days for US citizens. Passport must be valid 6 months.",
    "india": "e-Visa required. Apply online 4 days before travel. $25 fee. 30-day validity.",
    "france": "Schengen visa-free for 90 days within 180-day period for US citizens.",
    "thailand": "Visa on arrival for 30 days. $35 fee. Proof of onward travel required.",
}

PLACES_DB = {
    "japan": "Top spots: Tokyo (Shibuya, Asakusa), Kyoto (Fushimi Inari, Arashiyama), Osaka (Dotonbori), Mt. Fuji.",
    "india": "Top spots: Delhi (Red Fort), Agra (Taj Mahal), Jaipur (Amber Fort), Goa (beaches), Varanasi (Ganges).",
    "france": "Top spots: Paris (Eiffel Tower, Louvre), Nice (Riviera), Bordeaux (wine country), Mont Saint-Michel.",
    "thailand": "Top spots: Bangkok (Grand Palace), Chiang Mai (temples), Phuket (beaches), Ayutthaya (ruins).",
}

FLIGHTS_DB = {
    ("sfo", "japan"): "UA837 SFO-NRT roundtrip $780, departs 10:30am, returns 6pm.",
    ("lax", "japan"): "NH107 LAX-HND roundtrip $920, departs 11:45am, returns 4:30pm.",
    ("sfo", "india"): "AI174 SFO-DEL roundtrip $1100, departs 9:15pm, returns 1am.",
    ("jfk", "india"): "EK234 JFK-DEL via DXB roundtrip $980, departs 10pm, returns 8am.",
    ("sfo", "france"): "AF83 SFO-CDG roundtrip $720, departs 4:30pm, returns 11am.",
    ("jfk", "france"): "DL264 JFK-CDG roundtrip $650, departs 9:45pm, returns 1:30pm.",
    ("lax", "thailand"): "TG795 LAX-BKK roundtrip $890, departs 11:30pm, returns 6am.",
    ("jfk", "thailand"): "QR728 JFK-BKK via DOH roundtrip $1050, departs 8pm, returns 5am.",
}

HOTELS_DB = {
    "japan": "Hotels: Park Hyatt Tokyo ($450/night), Hoshinoya Kyoto ($800/night), Hotel Granvia Osaka ($180/night).",
    "india": "Hotels: Taj Mahal Palace Mumbai ($350/night), Oberoi New Delhi ($400/night), Rambagh Palace Jaipur ($550/night).",
    "france": "Hotels: Le Meurice Paris ($900/night), Hotel Negresco Nice ($400/night), InterContinental Bordeaux ($300/night).",
    "thailand": "Hotels: Mandarin Oriental Bangkok ($500/night), Four Seasons Chiang Mai ($700/night), Amanpuri Phuket ($1200/night).",
}

ITINERARY_TEMPLATES = {
    "japan": "Day 1: Tokyo arrival, Shibuya. Day 2: Asakusa, Senso-ji. Day 3: Bullet train to Kyoto, Fushimi Inari. Day 4: Arashiyama bamboo grove. Day 5: Osaka, Dotonbori.",
    "india": "Day 1: Delhi arrival, Red Fort. Day 2: Agra, Taj Mahal. Day 3: Jaipur, Amber Fort. Day 4: Udaipur lakes. Day 5: Return via Delhi.",
    "france": "Day 1: Paris arrival, Eiffel Tower. Day 2: Louvre, Seine cruise. Day 3: Versailles day trip. Day 4: TGV to Nice. Day 5: Riviera coast.",
    "thailand": "Day 1: Bangkok, Grand Palace. Day 2: Wat Arun, floating market. Day 3: Fly to Chiang Mai, temples. Day 4: Elephant sanctuary. Day 5: Phuket beach.",
}

EMAIL_LOG = []