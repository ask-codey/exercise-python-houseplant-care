# Exercise: Houseplant Care

Exercise code for the lesson **Exercise: Houseplant Care** in the Python in Depth course on [ask-codey.com](https://www.ask-codey.com).

Leaf & Sprout, a houseplant care app, needs the code that knows when each plant needs water: a `Plant` class, a `Cactus` that rests in winter, a `CareLog` dataclass that records each watering, and a function that lists the plants to water today. You'll write them in `plants.py`, and tests make plants and check what your code gives back.

## What's here

- `plants.py`: the `Plant` class, the `Cactus` subclass, the `CareLog` dataclass and the function `plants_to_water`. Each method you write stops with `NotImplementedError: Not built yet.` for now, and `CareLog` has only its first field. The docstring under each one says what it should do, with examples. For you to finish.
- `care_today.py`: prints Leaf & Sprout's plants, today's watering list and a care log with your code, so you can see it at work. Ready to use.
- `tests/test_plants.py`: tests that make plants and check what your code gives back. You don't need to change this file.
- `requirements.txt`: the one package the tests need, pytest, at an exact version. Ready to use.
- `pytest.ini`: tells pytest where the tests are and where to find `plants.py`. Ready to use.
- `.gitignore`: tells Git to leave out the virtual environment and the files Python and pytest make as they run. Ready to use.

## Before you start

The tests need pytest, and pytest goes in a virtual environment: a private set of packages for this folder only. In VS Code's terminal, in this folder, run these three commands.

On Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

On a Mac (zsh):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

- The first command makes the virtual environment, in a folder named `.venv`.
- The second turns it on for this terminal: the prompt starts with `(.venv)` from then on.
- The third installs the packages `requirements.txt` lists into it: here, only pytest.

*Virtual Environments and pip* explains all three. The `.venv` folder is in `.gitignore`, so Git leaves it out: these commands make it again on any computer.

If PowerShell answers that running scripts is disabled on this system, run this once, then run the second command again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Each new terminal starts with the virtual environment off. If the prompt doesn't start with `(.venv)`, run the second command again. (VS Code often turns it on for you.)

## Check your work

```bash
pytest
```

At first every test fails: that is expected, because each method stops with a `NotImplementedError` for now. Each piece you finish turns its tests green. A failing test's message says what it did, what it expected and what came back, for example *Plant('Fern', 3, May 7).needs_water(May 10) should give True, but it gave False.*

To see your code at work, run:

```bash
python care_today.py
```

## The rules

- Keep each class's name, each method's name and each function's name and parameters as they are. `Plant`'s `__init__` is written for you.
- `Cactus` is a subclass of `Plant`: set it up with `super().__init__()`, and let it use `Plant`'s methods wherever the cactus rule is the same.
- `CareLog` stays a dataclass, with its three fields in the order its docstring gives.
- Return each answer; don't print it. The tests read what your code gives back.
- Don't change the tests or `care_today.py`.

## Tips

- Work one example through by hand before you write the code: a fern watered every 3 days, last watered on May 7, needs water on May 10, because 3 days have passed.
- Subtracting one date from another gives the gap between them, and its `.days` is a whole number of days: `(today - self.last_watered).days`.
- A date's `.month` is its month as a number, 1 for January to 12 for December.
- `super().needs_water(today)` asks `Plant`'s version of the method, so the cactus doesn't have to repeat the usual rule.
- A list field in a dataclass needs `field(default_factory=list)`, so each log gets its own list.
- `plants_to_water` doesn't need to know which plants are cacti: each plant answers `needs_water` in its own way.

## Hand it in

When it works, push your solution to a public repo of your own on GitHub, then paste that repo's address into **Submit your exercise** on the lesson page at [ask-codey.com](https://www.ask-codey.com). That's what completes the lesson. The lesson page shows the Git commands, step by step.
