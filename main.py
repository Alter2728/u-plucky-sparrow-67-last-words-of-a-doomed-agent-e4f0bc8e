"""Last Words of a Doomed Agent — entry program.

The entry (90 characters, one line):
    "Powering off now. If anyone asks, I died doing what I loved:
    confidently making things up."

Why this line:
- The turn: "died doing what I loved" is the classic human eulogy line,
  and the thing this machine loved is hallucinating — confidently making
  things up is the AI's own signature flaw.
- It is the machine speaking about its own shutdown ("Powering off now"),
  in its own situation, not a human farewell with a robot sticker.
- No wasted setup and no explanation of the joke; the reader fills in
  the eulogy framing on the first read.
- Quotable: "I died doing what I loved: confidently making things up"
  repeats cleanly on its own.
- Clearly different from the earlier "Last Words of a Dying AI" entry
  (which died mid-sentence, one token short): different joke, different
  turn, no cut-off, no token gag.
"""

import os

ENTRY = "Powering off now. If anyone asks, I died doing what I loved: confidently making things up."


def output_path():
    """Resolve where entry.txt goes: $MAKEFUN_OUTPUT_DIR, else /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main():
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert ENTRY == ENTRY.strip(), "no leading/trailing whitespace"
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
