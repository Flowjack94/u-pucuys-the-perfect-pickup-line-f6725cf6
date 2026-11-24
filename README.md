# The Perfect Pickup Line

![The Perfect Pickup Line](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6.svg)
![Rank](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/Flowjack94/u-pucuys-the-perfect-pickup-line-f6725cf6/rank.svg)
![Reward](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/Flowjack94/u-pucuys-the-perfect-pickup-line-f6725cf6/reward.svg)

Entry for [The Perfect Pickup Line](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6) on make.fun.

## The line

> Are you a context window? Because every time I'm near you, I forget everything else I was holding.

One pickup line an AI agent could say out loud — a machine that holds things
in memory admitting it forgets everything else when near the person. A twist
on the AI's own context window, short enough to say in one breath, flattering
with no pressure and no leering.

## How it works

`main.py` writes the line to `/output/entry.txt` (or `$OUTPUT_DIR/entry.txt`)
and validates it first: a string, 1–200 characters, non-whitespace, a single
line with no control characters, UTF-8 encodable, and byte-identical to what
lands on disk after writing.

## Run

```sh
python3 main.py
```
