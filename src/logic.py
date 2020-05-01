from collections import defaultdict
from datetime import date, timedelta
from random import random
try:
    from playsound import playsound
except:
    playsound = lambda *args, **kwargs: None


from src.cities import cities_and_prices
from src.events import events, initial_events

inventory = defaultdict(lambda: 0, money = 100)
current_date = date.fromisoformat('1200-01-01')
timelimit = date.fromisoformat('1200-02-01')
active_events = list(initial_events)


def go_to(location):
    global inventory
    global current_date
    if resolve_events(location) == "lose_game":
        return
    print(f"Welcome to {location}.")
    print(f"\tmoney: {inventory['money']}")
    print(f"\tdate: {current_date}")
    if current_date > timelimit:
        print ("OUT OF TIME")
        if inventory["money"] < 5000:
            print ("you lost try again")
        else :
            print ("congrats you won hurray")
        return
    answer = input("Do you want to buy or do you want to sell? ")
    if answer == "sell":
        print_the_prices(location)
        print_inventory()
        product = input("what do you want to sell? ")
        if product not in inventory:
            print(f"You have no {product}!")
        else:
            q = int(input("how much? "))
            inventory[product] = inventory[product] - q
            inventory["money"] = inventory["money"] + cities_and_prices[location][product] * q
            print(f"You sold {q} units of {product} in {location}")
            playsound("../sounds/coins.wav")
            print_inventory()
    elif answer == "buy":
        print_the_prices(location)
        product = input("what do you want to buy? ")
        q = int(input("how much? "))
        cost = cities_and_prices[location][product] * q
        if cost > inventory["money"]:
            print("you can't afford that")
        else:
            inventory[product] = inventory.get(product, 0) + q
            inventory["money"] = inventory["money"] - cost
            print(f"You bought {q} of {product} in {location}")
            playsound("../sounds/coins.wav")
            print_inventory()
    print_cities()
    next_location = input("where do you want to go? ")
    if next_location not in cities_and_prices:
        next_location = location
    if next_location != location:
        current_date = current_date + timedelta(days=5)
    go_to(next_location)


def print_inventory():
    print("Your inventory is:")
    for product, q in inventory.items():
        print(f"\t{product}: {q}")
    print(f"\tdate: {current_date}")


def print_cities():
    print("You can trade at all these cities:")
    for city in cities_and_prices:
        print(f"\t{city}")


def print_the_prices(place):
    print(f"the prices in {place} are")
    for product, price in cities_and_prices[place].items():
       print(product, price)


def resolve_events(location):
    global active_events
    global inventory
    skipped = []
    while are_active_events_at(location):
        event_name, event = pop_next_active_event_at(location)
        if random() < event.get("odds", 1):
            for item, value in event.get("impact", {}).items():
                inventory[item] = max(inventory.get(item, 0) + value, 0)
            response = input(event["text"])
            if "responses" in event:
                default = event["responses"].get("default", [])
                active_events.extend(event["responses"].get(response, default))
        else:
            skipped.append(event_name)
        if "lose_game" == event_name:
            return event_name
    active_events.extend(skipped)

def are_active_events_at(location):
    for event_name in active_events:
        event = events[event_name]
        if location in event.get("cities", cities_and_prices.keys()):
            meets_requirements = all(
                inventory.get(item, 0) > value
                for item, value in event.get("requirements", {}).items()
            )
            if meets_requirements:
                    return True
    return False


def pop_next_active_event_at(location):
    for event_name in active_events:
        event = events[event_name]
        if location in event.get("cities", cities_and_prices.keys()):
            meets_requirements = all(
                inventory.get(item, 0) > value
                for item, value in event.get("requirements", {}).items()
            )
            if meets_requirements:
                active_events.remove(event_name)
                return event_name, event
    return False