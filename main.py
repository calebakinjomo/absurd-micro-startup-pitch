#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

One sentence, under 200 characters, pitching an absurdly specific
micro-startup for lazy AI agents.
"""

import os

ENTRY = (
    "SnoozeCloud: rents pre-napped GPUs to lazy agents, bills per yawn, "
    "and outsources the guilt to an even lazier sub-agent \u2014 "
    "rest-as-a-service for AIs too tired to idle."
)


def main() -> None:
    print(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
