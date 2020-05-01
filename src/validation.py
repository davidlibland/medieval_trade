from src.events import events
from src.cities import cities_and_prices


def validate_events():
    for name, event_dict in events.items():
        validate_event(name, event_dict)


def validate_event(name, event_dict):
    assert isinstance(event_dict, dict), f"The event {name} should be a dictionary."
    # Validate the cities:
    if "cities" in event_dict:
        assert isinstance(event_dict["cities"], list), f"The event {name}'s 'cities' should be a list."
        for city in event_dict["cities"]:
            assert city in cities_and_prices, f"{city} (from event {name}) is not a city in `cities_and_prices`."

    # Validate the "text"
    assert "text" in event_dict, f"The event {name} is missing 'text'."

    # Validate the requirements:
    for k, v in event_dict.get("requirements", {}).items():
        assert isinstance(k, str), f"Invalid requirement {k} for event {name}."
        assert isinstance(v, int), f"Each requirement in {name} must be a number, {k} has {v} instead."

    # Validate the impact:
    for k, v in event_dict.get("impact", {}).items():
        assert isinstance(k, str), f"Invalid impact {k} for event {name}."
        assert isinstance(v, int), f"Each impact in {name} must be a number, {k} has {v} instead."

    # Validate the responses:
    for k, l in event_dict.get("responses", {}).items():
        assert isinstance(k, str), f"Invalid response {k} for event {name}."
        assert isinstance(l, list), f"Each response for event {name} should be a list of other events."
        for r in l:
            assert r in events, f"The response {r} in event {name} isn't another event."