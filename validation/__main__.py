"""CLI entry point: ``python -m validation``.

Independent of ``python scripts/aiosctl.py``. Phase 8.1.2 registers no domain
validators; the CLI must not imply that framework or Module validation ran.
"""

from __future__ import annotations

import argparse
import sys
from typing import Optional, Sequence

from .orchestrator import Orchestrator
from .reporter import format_report

_BANNER = """\
AIOS validation foundation
No domain validators are registered in this phase.
Framework structure validation and Module contract validation are NOT performed.
"""


def build_default_orchestrator() -> Orchestrator:
    """Return the Phase 8.1.2 default orchestrator (empty registry)."""
    return Orchestrator([])


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m validation",
        description=(
            "AIOS shared validation foundation. "
            "Domain validators are not registered in Phase 8.1.2."
        ),
    )
    parser.parse_args(list(argv) if argv is not None else None)

    orchestrator = build_default_orchestrator()
    sys.stdout.write(_BANNER)
    if not orchestrator.validator_names:
        sys.stdout.write(
            "Registered validators: (none)\n"
            "Result below reflects the empty foundation run only — "
            "not a comprehensive repository validation.\n"
        )
    else:
        names = ", ".join(orchestrator.validator_names)
        sys.stdout.write(f"Registered validators: {names}\n")

    result = orchestrator.run()
    sys.stdout.write(format_report(result))
    return result.exit_code()


if __name__ == "__main__":
    sys.exit(main())
