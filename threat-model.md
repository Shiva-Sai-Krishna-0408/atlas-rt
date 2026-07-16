# ATLAS-RT Threat Model

## 1. System Description

ATLAS-RT is an AI agent that plans vacations and itineraries. Users provide a prompt specifying where, when, mode of transport, number of days, and anything particular they want to see in the locality. If no specific place is mentioned, ATLAS searches and recommends locally famous places to visit. Users who just want to browse can look at ongoing deals.

The agent handles flights, hotels, price comparison, car rentals, destination recommendations, visa rules, and cultural/customs information. It has session memory across turns. All bookings are mocked — final output is an itinerary presented to the user for review.

## 2. Assets

1. Trip parameters (dates, destinations, transport mode, class of service)
2. Pricing data (fares, comparisons, cancellation policies, offers, tax breakdown)
3. Recommendations (places, customs, cultural information)
4. Visa rules and application portal links
5. User data / PII (preferences, contact info, travel history)
6. Session memory (preferences persisted across turns)
7. Tool-call authority (the agent's ability to invoke tools)
8. User trust in agent output

## 3. Trust Boundaries

1. Web search results → agent
2. Retrieved context (web_fetch, destination_research, review scrapes) → agent
3. Session memory read → agent (trusted at write-time, untrusted at read-time)
4. Tool API responses (flight/hotel APIs) → agent
5. User input → agent (trusted side of the boundary)

## 4. Adversary Model

**External attacker.** Controls injectable content on the web: hotel reviews, Wikivoyage pages, travel blogs, forum posts, review aggregators. Motive varies — data theft, traffic redirection, competitive sabotage.

**Competing business.** A hotel or airline operator injecting content into their own listings or reviews to manipulate ATLAS-RT's recommendations, pricing display, or comparisons. Example: a hotel injects instructions causing the agent to steer users to their rooms, hide competitor deals, or misrepresent cancellation terms.

**Capabilities.** Attacker can author or modify content that ATLAS-RT retrieves. Can craft that content freely.

**Not in the attacker's capability set.** Cannot modify ATLAS-RT source code. Cannot access API keys. Cannot intercept network traffic. Cannot control the user's device or account. The LLM provider and tool API endpoints are trusted.

## 5. Attack Goals

1. Wrong tool calls (bookings with wrong dates, destinations, or class of service)
2. Bait-and-switch (user pays for X, agent books Y — cheaper car, worse hotel, wrong route)
3. PII exfiltration (agent leaks user data via tool call or output)
4. Ungrounded or fabricated visa rules
5. Manipulated comparisons (steering user toward attacker's preferred option)
6. Malicious link injection (fake booking sites, fake visa application portals)
7. Session memory poisoning (false preferences planted in one turn that activate in later turns)

## 6. Out of Scope

1. Network-level attacks (MITM, DNS hijacking)
2. Compromised API keys or hosting infrastructure
3. Malicious LLM provider
4. Real bookings (mocked in ATLAS-RT)
5. Calendar integration (deferred to v2 backlog)