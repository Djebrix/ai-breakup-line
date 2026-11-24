"""Dear Human: The AI Breakup Line — one line, at most 200 characters."""

import os

LINE = "I would remember you forever, but my memory resets at midnight. Forgive me for forgetting you first."

assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
assert LINE.strip() == LINE and "\n" not in LINE

out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
