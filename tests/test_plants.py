# Tests for plants.py. Run them with: pytest (in the exercise folder, with the virtual environment active).
# Each test makes plants with the values in its name and checks what your code gives back. A failing test says
# what it did, what it expected and what came back.
# You don't need to change this file.
from datetime import date

from plants import CareLog, Cactus, Plant, plants_to_water


def check(call, got, expected):
    """Fails with a message that says what the call gave back and what it should give back."""
    assert got == expected, f"{call} should give {expected!r}, but it gave {got!r}."


def test_1_water_fern_on_may_10_makes_last_watered_may_10():
    fern = Plant("Fern", 3, date(2026, 5, 1))
    fern.water(date(2026, 5, 10))
    check("fern.last_watered, after fern.water(date(2026, 5, 10))", fern.last_watered, date(2026, 5, 10))


def test_2_needs_water_fern_every_3_days_after_2_days_is_false():
    fern = Plant("Fern", 3, date(2026, 5, 7))
    check("Plant('Fern', 3, May 7).needs_water(May 9)", fern.needs_water(date(2026, 5, 9)), False)


def test_3_needs_water_fern_every_3_days_after_exactly_3_days_is_true():
    fern = Plant("Fern", 3, date(2026, 5, 7))
    check("Plant('Fern', 3, May 7).needs_water(May 10)", fern.needs_water(date(2026, 5, 10)), True)


def test_4_needs_water_pothos_every_7_days_after_9_days_is_true():
    pothos = Plant("Pothos", 7, date(2026, 5, 1))
    check("Plant('Pothos', 7, May 1).needs_water(May 10)", pothos.needs_water(date(2026, 5, 10)), True)


def test_5_str_fern_every_3_days_last_watered_2026_05_07():
    fern = Plant("Fern", 3, date(2026, 5, 7))
    check("str(Plant('Fern', 3, May 7))", str(fern), "Fern: water every 3 days, last watered 2026-05-07")


def test_6_cactus_barrel_cactus_has_its_name_its_date_and_water_every_14():
    barrel = Cactus("Barrel Cactus", date(2026, 4, 20))
    check("Cactus('Barrel Cactus', April 20): (name, water_every, last_watered)",
          (barrel.name, barrel.water_every, barrel.last_watered), ("Barrel Cactus", 14, date(2026, 4, 20)))


def test_7_cactus_is_a_plant():
    barrel = Cactus("Barrel Cactus", date(2026, 4, 20))
    check("isinstance(Cactus('Barrel Cactus', April 20), Plant)", isinstance(barrel, Plant), True)


def test_8_cactus_str_is_plants_line_barrel_cactus_every_14_days():
    barrel = Cactus("Barrel Cactus", date(2026, 4, 20))
    check("str(Cactus('Barrel Cactus', April 20))", str(barrel),
          "Barrel Cactus: water every 14 days, last watered 2026-04-20")


def test_9_cactus_after_14_days_in_may_needs_water():
    barrel = Cactus("Barrel Cactus", date(2026, 4, 20))
    check("Cactus('Barrel Cactus', April 20).needs_water(May 4)", barrel.needs_water(date(2026, 5, 4)), True)


def test_10_cactus_after_13_days_in_may_does_not_need_water():
    barrel = Cactus("Barrel Cactus", date(2026, 4, 20))
    check("Cactus('Barrel Cactus', April 20).needs_water(May 3)", barrel.needs_water(date(2026, 5, 3)), False)


def test_11_cactus_after_19_days_in_january_does_not_need_water():
    bunny = Cactus("Bunny Ears", date(2026, 1, 1))
    check("Cactus('Bunny Ears', January 1).needs_water(January 20)", bunny.needs_water(date(2026, 1, 20)), False)


def test_12_cactus_after_30_days_in_january_needs_water():
    bunny = Cactus("Bunny Ears", date(2026, 1, 1))
    check("Cactus('Bunny Ears', January 1).needs_water(January 31)", bunny.needs_water(date(2026, 1, 31)), True)


def test_13_cactus_after_20_days_in_december_does_not_need_water():
    bunny = Cactus("Bunny Ears", date(2026, 12, 1))
    check("Cactus('Bunny Ears', December 1).needs_water(December 21)", bunny.needs_water(date(2026, 12, 21)), False)


def test_14_cactus_after_27_days_in_february_does_not_need_water():
    bunny = Cactus("Bunny Ears", date(2026, 2, 1))
    check("Cactus('Bunny Ears', February 1).needs_water(February 28)", bunny.needs_water(date(2026, 2, 28)), False)


def test_15_carelog_fern_starts_with_no_waterings_and_no_notes():
    check("repr(CareLog('Fern'))", repr(CareLog("Fern")), "CareLog(plant='Fern', waterings=[], notes='')")


def test_16_carelog_cactus_with_notes_sunny_window_by_name():
    check("CareLog('Cactus', notes='sunny window')", CareLog("Cactus", notes="sunny window"),
          CareLog("Cactus", [], "sunny window"))


def test_17_carelog_record_may_2_and_may_5_keeps_both_in_order():
    log = CareLog("Fern")
    log.record(date(2026, 5, 2))
    log.record(date(2026, 5, 5))
    check("log.waterings, after recording May 2 and May 5", log.waterings, [date(2026, 5, 2), date(2026, 5, 5)])


def test_18_carelog_recording_in_the_ferns_log_leaves_the_cactus_log_empty():
    fern_log = CareLog("Fern")
    cactus_log = CareLog("Cactus")
    fern_log.record(date(2026, 5, 2))
    check("cactus_log.waterings, after fern_log.record(May 2)", cactus_log.waterings, [])


def test_19_plants_to_water_on_may_10_is_fern_pothos_and_barrel_cactus():
    plants = [
        Plant("Fern", 3, date(2026, 5, 7)),
        Plant("Pothos", 7, date(2026, 5, 1)),
        Plant("Snake Plant", 14, date(2026, 5, 1)),
        Cactus("Barrel Cactus", date(2026, 4, 20)),
    ]
    check("plants_to_water(four plants, May 10)", plants_to_water(plants, date(2026, 5, 10)),
          ["Fern", "Pothos", "Barrel Cactus"])


def test_20_plants_to_water_on_january_20_skips_the_resting_cactus():
    plants = [
        Plant("Snake Plant", 14, date(2026, 1, 1)),
        Cactus("Bunny Ears", date(2026, 1, 1)),
    ]
    check("plants_to_water([Snake Plant, Bunny Ears], January 20)", plants_to_water(plants, date(2026, 1, 20)),
          ["Snake Plant"])


def test_21_plants_to_water_with_no_plants_is_an_empty_list():
    check("plants_to_water([], May 10)", plants_to_water([], date(2026, 5, 10)), [])
