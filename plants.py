"""Leaf & Sprout's houseplant care: two classes, a dataclass and a function for you to finish.

The docstring under each one says what it should do, with examples.
Replace each raise NotImplementedError("Not built yet.") line with your own
code. Return each answer: the tests read what comes back, not what's printed.
"""
from dataclasses import dataclass, field
from datetime import date


class Plant:
    """One houseplant: its name, how many days it goes between waterings, and the date it was last watered.

    __init__ is ready to use. Finish water, needs_water and __str__.
    """

    def __init__(self, name, water_every, last_watered):
        self.name = name
        self.water_every = water_every
        self.last_watered = last_watered

    def water(self, today):
        """Record that the plant was watered today: its last_watered becomes today.

        fern = Plant("Fern", 3, date(2026, 5, 1))
        fern.water(date(2026, 5, 10))   -> fern.last_watered is now date(2026, 5, 10)
        """
        raise NotImplementedError("Not built yet.")

    def needs_water(self, today):
        """Return True when at least water_every days have passed since last_watered, and False when fewer have.

        (today - self.last_watered).days is the number of days between the two dates.

        fern = Plant("Fern", 3, date(2026, 5, 7))
        fern.needs_water(date(2026, 5, 9))    -> False  (2 days)
        fern.needs_water(date(2026, 5, 10))   -> True   (3 days: exactly enough counts)
        """
        raise NotImplementedError("Not built yet.")

    def __str__(self):
        """Return the plant's line: its name, how often it's watered and when it was last watered.

        str(Plant("Fern", 3, date(2026, 5, 7)))
            -> "Fern: water every 3 days, last watered 2026-05-07"
        """
        raise NotImplementedError("Not built yet.")


class Cactus(Plant):
    """A cactus: a Plant that goes 14 days between waterings, and longer in winter.

    Cactus(name, last_watered) takes no water_every, because a cactus always goes
    14 days between waterings.

    Cactus("Barrel Cactus", date(2026, 4, 20)).water_every   -> 14
    """

    def __init__(self, name, last_watered):
        """Set the cactus up as a Plant that goes 14 days between waterings, with super()."""
        raise NotImplementedError("Not built yet.")

    def needs_water(self, today):
        """Return True when the cactus needs water today, and False when it doesn't.

        In December, January and February a cactus rests, so it needs water only
        once at least 30 days have passed. In every other month it follows Plant's
        rule: at least 14 days.

        barrel = Cactus("Barrel Cactus", date(2026, 4, 20))
        barrel.needs_water(date(2026, 5, 4))     -> True   (14 days, in May)
        bunny = Cactus("Bunny Ears", date(2026, 1, 1))
        bunny.needs_water(date(2026, 1, 20))     -> False  (19 days, in January: it waits for 30)
        bunny.needs_water(date(2026, 1, 31))     -> True   (30 days)
        """
        raise NotImplementedError("Not built yet.")


@dataclass
class CareLog:
    """A plant's care log, written as a dataclass with three fields, in this order:

    plant       the plant's name, a str, with no default (written for you)
    waterings   the dates the plant was watered, a list of dates (list[date])
                that starts empty: a new list for each log
    notes       a str, "" when a log is made without notes

    CareLog("Fern")                          -> CareLog(plant='Fern', waterings=[], notes='')
    CareLog("Cactus", notes="sunny window")  -> CareLog(plant='Cactus', waterings=[], notes='sunny window')
    """

    plant: str
    # Add the other two fields here: waterings and notes.

    def record(self, day):
        """Add day to the end of this log's waterings.

        log = CareLog("Fern")
        log.record(date(2026, 5, 2))
        log.record(date(2026, 5, 5))
        log.waterings   -> [date(2026, 5, 2), date(2026, 5, 5)]
        """
        raise NotImplementedError("Not built yet.")


def plants_to_water(plants, today):
    """Return a list of the names of the plants that need water today, in the list's order.

    Ask each plant with its own needs_water, so a Cactus answers with the cactus rule.
    An empty list of plants gives an empty list.

    plants = [Plant("Fern", 3, date(2026, 5, 7)),
              Plant("Snake Plant", 14, date(2026, 5, 1)),
              Cactus("Barrel Cactus", date(2026, 4, 20))]
    plants_to_water(plants, date(2026, 5, 10))   -> ["Fern", "Barrel Cactus"]
    """
    raise NotImplementedError("Not built yet.")
