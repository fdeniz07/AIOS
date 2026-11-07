"""CLI entry point: ``python -m validation``.

Independent of ``python scripts/aiosctl.py``.
Phase 8.2 registers Framework Structure Validation by default.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Optional, Sequence

from .framework_structure import make_framework_structure_runner
from .orchestrator import Orchestrator
from .reporter import format_report

_BANNER = """\
AIOS validation
Registered validator: framework-structure (Framework Structure Validation)
Module contract validation and documentation integrity are NOT performed.
"""


def build_default_orchestrator(
    *,
    explicit_root: Optional[Path] = None,
) -> Orchestrator:
    """Return the default orchestrator with Framework Structure Validation."""
    orchestrator = Orchestrator()
    orchestrator.register(
        "framework-structure",
        make_framework_structure_runner(explicit_root=explicit_root),
    )
    return orchestrator


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m validation",
        description=(
            "AIOS validation. "
            "Runs Framework Structure Validation by default."
        ),
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help="Explicit Framework root directory to validate",
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    orchestrator = build_default_orchestrator(explicit_root=args.root)
    sys.stdout.write(_BANNER)
    names = ", ".join(orchestrator.validator_names)
    sys.stdout.write(f"Registered validators: {names}\n")
    if args.root is not None:
        sys.stdout.write(f"Explicit root: {args.root}\n")

    result = orchestrator.run()
    sys.stdout.write(format_report(result))
    return result.exit_code()


if __name__ == "__main__":
    sys.exit(main())
