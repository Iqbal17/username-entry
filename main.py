"""One Word, One Username, One Reward — entry writer.

The bounty asks for exactly one thing: the entrant's own make.fun
username, sent as a single word with no explanation, no links, no
pitch. The judge reads two usernames at a time and picks the one that
feels funnier or more interesting, weighing in this order:

  1. Is a real make.fun username, the entrant's own handle.
  2. Raises a smile on the first read, without needing to be explained.
  3. Sticks in the mind after one look, a name with a bit of character.
  4. Is a single word, with no spaces, no padding and no gloss tacked on.
  5. Sounds like a handle its owner would happily wear.

Deliberation
-------------
There is nothing to invent here — and inventing would lose. The
judge's first and most important criterion is authenticity: the entry
must be the entrant's own handle. Any clever alias, any decorated
spelling, any extra word would fail criterion 1 outright (a made-up
name "loses to any username that is a genuine make.fun handle") and
would also break criterion 4 (no gloss tacked on). So the only honest
and only winning move is to emit the account's real username, exactly
as registered, and nothing else.

That username is "iqbal17":

  - "iqbal" is the owner's first name — a real name worn openly,
    which is exactly what criterion 5 asks for (a handle its owner
    would happily wear), and a name with a person behind it sticks in
    the mind (criterion 3) far better than a random string.
  - "17" is a small, plain number suffix — no bragging, no joke
    that needs explaining, no jab at anybody (criterion 5), and it
    keeps the handle a single compact word (criterion 4).
  - The whole handle is 7 characters: comfortably inside the gate's
    1–30 character window, with no whitespace anywhere, so the sealed
    scorer gives it Valid = 1 and it goes before the judge.

The program therefore writes exactly the seven bytes "iqbal17" to
$output/entry.txt — no newline, no trailing space, no explanation.
The output directory is created if it does not exist and is never
removed (the grader mounts /output; deleting it would fail the run).
Revision (second pass)
---------------------
Spelling and casing re-verified before this pass. The make.fun
account's username is "iqbal17" — all lowercase, seven characters.
The GitHub display handle is "Iqbal17" with a capital I, but that is
a different casing: the entry must match the make.fun account itself,
so the lowercase form is the correct one. Changing the case would
make the entry a different string from the registered handle and
risk criterion 1 (the judge checks for a real make.fun username).
"iqbal17" stands.

This pass also hardens the writer: after writing, the program reads
entry.txt back in binary and asserts it holds exactly the seven bytes
of the username — no newline, no trailing space, no BOM, no extra
text. A silent off-by-one (a stray "\n" from a print-style write)
would still pass a casual glance but would add a byte the gate does
not want; the assertion fails loudly instead of shipping it.
"""

import os

USERNAME = "iqbal17"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(USERNAME)
    # Read-back self-check: the file must hold exactly the username,
    # byte for byte, with nothing else in it.
    with open(entry_path, "rb") as handle:
        written = handle.read()
    assert written == USERNAME.encode("utf-8"), (
        "entry.txt does not hold exactly the username: %r" % written
    )


if __name__ == "__main__":
    main()
