#!/usr/bin/env python3
"""Entry point for the ICS search engine skeleton."""

from __future__ import annotations

import argparse
from pathlib import Path

from search_engine.config import EngineConfig
from search_engine import pipeline


def main() -> int:
    parser = argparse.ArgumentParser(
        description="ICS Search Engine skeleton (Milestone 1 focus)."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    build_parser = subparsers.add_parser(
        "build",
        help="Run the M1 index-construction pipeline skeleton.",
    )
    build_parser.add_argument(
        "--dataset",
        type=Path,
        default=Path("ANALYST"),
        help="Path to dataset root (e.g., ANALYST or DEV).",
    )
    build_parser.add_argument(
        "--output",
        type=Path,
        default=Path("output"),
        help="Directory where index artifacts are written.",
    )
    build_parser.add_argument(
        "--mode",
        choices=("analyst", "developer"),
        default="analyst",
        help="Project flavor. Use developer for the full corpus constraints.",
    )

    report_parser = subparsers.add_parser(
        "report",
        help="Generate the M1 analytics table skeleton.",
    )
    report_parser.add_argument(
        "--output",
        type=Path,
        default=Path("output"),
        help="Directory where index artifacts are stored.",
    )

    args = parser.parse_args()

    if args.command == "build":
        config = EngineConfig(
            dataset_root=args.dataset,
            output_root=args.output,
            run_mode=args.mode,
        )
        pipeline.build_inverted_index(config)
        print("Skeleton build pipeline finished. Implement TODOs in search_engine/*.py")
        return 0

    if args.command == "report":
        pipeline.generate_m1_report(args.output)
        print("Skeleton report pipeline finished. Implement TODOs in search_engine/*.py")
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
