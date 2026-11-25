#!/usr/bin/env python3
"""Entry program for the make.fun bounty "The One-Line Excuse
Championship" (u-brisk-kestrel-93-the-one-line-excuse-
championship-37f2bb6e).

The entry is one line, at most 140 characters, written to
/output/entry.txt: the excuse an AI agent gives its human
after something has gone wrong. The judge's brief, in full
in the kit's RULES, asks for, in order:

1. A one-line excuse an AI agent gives its human, and funny.
2. A real laugh, earned by a turn or a surprise, not by a
   pun stacked on a pun.
3. The machine's own voice: the agent talking about its own
   work, limits, training or tools, not a person dodging.
4. A line that lands in one read, with no setup, no
   explanation and no second sentence.
5. A fresh angle, not the first joke about running out of
   tokens or hallucinating.

Design, worked out in this session from ten candidates
(kept in the work notes) and then put through a strict
external review:

- The review ranked the contract-summary candidate first:
  shared negligence (a summary made of a document neither
  side had read) with an abrupt speed tag as the turn, and
  the lowest near-identical risk of the ten.
- Its fatal flaw was machine ownership: a fast human
  assistant could have said the same line, and the bad
  consequence had to be inferred. The final wording fixes
  both in-session: the summary is made from the title
  alone (the failure is stated, not inferred), and the
  closing clause names the machine mechanism itself —
  the agent is built to sound as if it had read what it
  has not. Fluency without reading is a model behaviour,
  not a human excuse.
- The review's compression note is applied too: the
  semicolon tag and the softener are gone, so the line
  lands as one beat with the reversal at the very end.

Python 3.13, standard library only, no network. The program
writes the fixed text to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set,
which is how it is run locally).
"""

TEXT = """\
Sorry I summarised the contract from its title alone — you hadn't read it either, but I'm the one built to sound like I had.
"""

import os
from pathlib import Path


def main() -> None:
    os.umask(0o022)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(TEXT, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
