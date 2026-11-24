"""Write the one-line pitch to /output/entry.txt.

Pure-stdlib, deterministic: the same bytes on every run.
"""

import os

SENTENCE = (
    "Just tell me the app idea you've been sitting on and I'll let an AI agent "
    "build a first working version of it for you on make.fun, free to try, and "
    "if you don't love it you've lost nothing but the telling."
)


def main():
    # Gate: the entry must be 1-240 characters, exactly one sentence.
    assert 1 <= len(SENTENCE) <= 240, f"sentence is {len(SENTENCE)} chars"
    assert SENTENCE.endswith("."), "sentence must end with a period"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
