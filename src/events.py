from src.cities import europe

initial_events = [
    "fez_pirates",
    "old_miner",
    "pirate_attack",
    "london_luxury_challenge",
    "shipwrecked",
    "meet_merek"
]

events = {
    "lose_game": {
        "text": "You lost the game."
    },
    "fez_pirates": {
        "cities": [
            "fez",
            "tunis"
        ],
        "requirements": {
            "money": 1000,
        },
        "text": "A pirate ship boards your vessel. They stole 1000 of your money",
        "impact": {
            "money": -1000
        },
    },
    "found_timbuktu_gold": {
        "cities": [
            "timbuktu",
        ],
        "requirements": {
            "money": 10
        },
        "text": "You found a buried treasure containing 10 gold and 3 gems",
        "impact": {
            "gold": +10,
            "gems": +3
        },"responses": {
            "default": ["king_comes"],
        }
    },
    "old_miner": {
        "cities": [
            "timbuktu",
        ],
        "text": "An old miner meets you, and says he knows where some buried treasure is. Do you follow him? ",
        "responses": {
            "default": [],
            "yes": ["found_timbuktu_gold"]
        }
    },
    "king_comes": {
        "cities": [
            "timbuktu",
        ],
        "text": "The king wants your gold. Do you stay or go? ",
        "responses": {
            "stay": ["lose_buried_treasure"]
        }
    },
    "lose_buried_treasure": {
        "cities": [
            "timbuktu",
        ],
        "text": "The king takes your treasure! ",
        "impact": {
            "gold": -10,
            "gems": -3
        }
    },
    "the_hanseatic_league_asks_you_to_join": {
        "cities": ["brandenburg", "hamburg"],
        "text": "you are asked to join the hanseatic league do you join? ",
        "responses": {
            "yes": ["gain_100_money"],
            "no": []
        }
    },
    "gain_100_money": {
        "text": "You gain 100 money",
        "impact": {
            "money": 100,
        }
    },
    "pirate_attack": {
        "text": "You were attacked by pirates!! ",
        "impact": {
            "money": -250,
        },
        "odds": 5/100,
        "responses": {
            "default": ["pirate_attack"],
        }
    },
    "shipwrecked": {
        "text": "You got shiprecked! Good thing your ship was insured. Pay insurense fee of 100. ",
        "impact": {
            "money": -100,
        },
        "odds": 10/120,
        "responses": {
            "default": ["shipwrecked"],
        }
    },
    "london_luxury_challenge": {
        "text": "The king of england feels england's markets are too backwards. He declares: 'I want these markets to "
                "sell more luxury goods! The first merchant who brings 1000 silk, gold, gems, or spices to this market will "
                "be knighted!'. Are you up for the challenge?",
        "cities": ["london"],
        "responses": {
            "default": ["london_silk_challenge", "london_gold_challenge", "london_gems_challenge", "london_spices_challenge"]
        }
    },
    "london_silk_challenge": {
        "text": "The king approaches you. 'What incredible silk! You will surely be knighted for this!'",
        "requirements": {
            "silk": 1000
        },
    },
    "london_gold_challenge": {
        "text": "The king approaches you. 'What incredible gold! You will surely be knighted for this!'",
        "requirements": {
            "gold": 1000
        },
    },
    "london_gems_challenge": {
        "text": "The king approaches you. 'What incredible gems! You will surely be knighted for this!'",
        "requirements": {
            "gems": 1000
        },
    },
    "london_spices_challenge": {
        "text": "The king approaches you. 'What incredible spices! You will surely be knighted for this!'",
        "requirements": {
            "spices": 1000
        },
    },

    "meet_merek": {
        "text": "You meet a man named Merek at the specialty market. He is the exact appearance of "
                "a gentleman. He asks \"Do you want to join the black marketeer guild? "
                "People pay guild members four times the amount for luxury goods. Whatever your "
                "reply, be sure not to tell Sheriff Carrack about this.\". Do you say yes or no?",
        "cities": europe,
        "odds": 50/100,
        "responses": {
            "default": ["reject_merek"],
            "yes": ["accept_merek", "good_prices", "carrack_catches_you"]
        }
    },
    "reject_merek": {
        "text": "\"Only a fool would say no to this offer! I hope you ship sinks "
                "or you get robbed by bandits!!\" responds Merek."
    },
    "accept_merek": {
        "text": "\"Make sure that Sheriff Carrack doesn't catch you!\""
    },
    "carrack_catches_you": {
        "odds": 5/100,
        "text": "You're at the black market with two other black marketeers, when suddenly "
                "Carrack's patrol comes with Carrack leading it. You're worried and you tell "
                "the other black marketeers to hide while you try to finish your sale quietly. But "
                "Carrack comes into the shop and discovers it's a black market. He yells \"You're "
                "under arrest!\" You try to flee, but his deputies have surrounded the stall. You're "
                "horrified. His deputies grab you. Then he says: \"I'm a fair sheriff, so I will give "
                "you a choice. You may give me half your money and tell me where the other black "
                "marketeers are, or you may die.\" Do you tell him (yes/no)?",
        "responses": {
            "default": ["lose_game"],
            "yes": ["carrack_takes_money", "black_marketeers_target_you"]
        }
    },

    # ToDo: Fix these:
    "good_prices": {
        "text": "Thanks to your black market connections, you get a great price.",
    },
    "carrack_takes_money": {
        "text": "Carrack takes your money."
    },
    "black_marketeers_target_you": {
        "text": "You are attacked by black marketeers."
    }
}