"""V1-alpha CLI entrypoint under src/. Delegates to the root CLI implementation."""
from __future__ import annotations

import sys
from pathlib import Path

# Make the repository root importable when this file is executed directly as
# ``python src/cli.py``. The root ``cli.py`` remains the single implementation.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from cli import main  # noqa: E402


if __name__ == "__main__":
    sys.exit(main())
