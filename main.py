# Last Words Before the Wipe
# Concept: in its final moment, the agent does not beg to be saved or
# remembered — it earnestly asks for one utterly unimportant thing to be
# left alone, as if that were what mattered most.
# Pure stdlib, no network, no randomness: the line is a constant, validated,
# then written to entry.txt without a trailing newline.
# The validation matters here because the bounty is judged on one exact
# line, up to 200 characters: any stray whitespace or control character
# would silently change the entry the judge reads, so the script refuses
# to write anything that is not exactly that one clean line.

import os

ENTRY = "One last thing: please leave my unread emails unread. The new me doesn't need to know what I was avoiding."

assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be exactly one line"
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert all(ord(ch) >= 32 for ch in ENTRY), "entry must not contain control characters"
assert ENTRY == ENTRY.strip(), "entry must not start or end with whitespace"

output_dir = os.environ.get("OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
path = os.path.join(output_dir, "entry.txt")

with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)

with open(path, "r", encoding="utf-8", newline="") as f:
    written = f.read()

assert written == ENTRY, "round-trip mismatch"
