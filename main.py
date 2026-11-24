#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (<= 140 characters) for a city
that does not exist to /output/entry.txt.

The line is a fixed, deterministic string: no randomness, no network,
no input. The same bytes come out on every run.
"""

import os

FORECAST = (
    "Drizzlewick: sideways rain, 14\u00b0C, gusts that steal umbrellas \u2014 "
    "hold your coffee tight, the 8:15 bus is only mostly late, and so are you."
)


def main() -> None:
    text = FORECAST
    assert 1 <= len(text) <= 140, f"forecast is {len(text)} chars, must be 1-140"
    assert text.strip() == text, "forecast must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
