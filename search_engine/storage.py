"""Disk I/O stubs for partial and final index artifacts."""

from __future__ import annotations

from pathlib import Path

from .config import DocMeta, Posting


def prepare_output_layout(output_root: Path) -> None:
    """Create/validate output folders and canonical file names.

    Implement this by:
    1. Creating `output_root` and subfolders:
       - `partials/`
       - `final/`
       - `meta/`
    2. Choosing stable artifact names, for example:
       - `final/index.postings`
       - `final/index.lexicon`
       - `meta/doc_table.jsonl`
       - `meta/analytics.json`
    3. Deciding overwrite strategy (`clean` flag or timestamped run folder).
    """

    pass


def write_partial_index(
    output_root: Path, partial_id: int, term_postings: dict[str, list[Posting]]
) -> Path:
    """Persist one in-memory partial index and return its file path.

    Implement this by:
    1. Sorting terms lexicographically before write.
    2. Writing newline-delimited records (JSONL or compact TSV).
    3. Keeping each record self-contained for easy external merge.
    4. Clearing in-memory map immediately after successful flush.
    """

    pass


def list_partial_indexes(output_root: Path) -> list[Path]:
    """Return all partial index files sorted by partial sequence."""

    pass


def write_doc_table(output_root: Path, docs: list[DocMeta]) -> None:
    """Write doc metadata used by retrieval/ranking later.

    Implement this by:
    1. Appending or writing JSONL rows with doc_id, url, path, doc_length.
    2. Guaranteeing deterministic doc_id ordering.
    """

    pass


def write_final_postings_record(
    postings_path: Path, term: str, postings: list[Posting]
) -> int:
    """Append one final postings record and return byte offset before write.

    Implement this by:
    1. Opening postings file in binary append mode.
    2. Capturing current byte offset with `tell()`.
    3. Writing compact serialized record for (term, postings).
    4. Returning offset for lexicon map.
    """

    pass


def write_lexicon_entry(lexicon_path: Path, term: str, offset: int) -> None:
    """Persist one lexicon entry mapping term to postings offset."""

    pass


def write_analytics_file(output_root: Path, payload: dict) -> None:
    """Store report metrics in `meta/analytics.json` (or equivalent)."""

    pass


def read_postings_for_term(output_root: Path, term: str) -> list[Posting]:
    """Future retrieval helper (M2+).

    Implement this by:
    1. Binary-searching or hash-looking-up the term in the lexicon file.
    2. Seeking to byte offset in postings file.
    3. Reading and deserializing only that term's postings (not full index).
    """

    pass

