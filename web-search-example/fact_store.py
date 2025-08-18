#!/usr/bin/python3

import os
import json
from config import FACT_FILE

def load_facts():
    if not os.path.exists(FACT_FILE):
        example_facts = {
            "Moon landing 1969": "The Apollo 11 mission landed the first humans on the Moon on July 20, 1969.",
            "Fall of Berlin Wall": "The Berlin Wall fell on November 9, 1989, marking the symbolic end of the Cold War."
        }
        with open(FACT_FILE, "w") as f:
            json.dump(example_facts, f, indent=2)
    with open(FACT_FILE, "r") as f:
        return json.load(f)

