"""Configuration and shared typed structures for the search engine."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal


@dataclass(slots=True)
class EngineConfig:
    """Runtime settings for index construction.

    Notes:
    - `partial_flush_docs` and `min_partial_flushes` are here to enforce the
      developer-option requirement of writing partial indexes to disk multiple
      times before merge.
    - Keep all index outputs file-based (no DB) so this config works for both
      analyst and developer flavors.
    """

    dataset_root: Path
    output_root: Path
    run_mode: Literal["analyst", "developer"]
    partial_flush_docs: int = 1500
    min_partial_flushes: int = 3
    token_regex: str = r"[A-Za-z0-9]+"
    title_boost: float = 3.0
    heading_boost: float = 2.0
    bold_boost: float = 1.5


@dataclass(slots=True)
class Posting:
    """Posting payload for a term in one document.

    M1 minimum requirement:
    - store `doc_id`
    - store raw `tf` (term frequency)

    Keep `important_hits` now, because M2/M3 ranking needs boosted fields.
    """

    doc_id: int
    tf: int
    important_hits: int


@dataclass(slots=True)
class DocMeta:
    """Per-document metadata.

    Keep this small and append-only so it can live in a compact sidecar file.
    """

    doc_id: int
    url: str
    source_path: str
    doc_length: int


@dataclass(slots=True)
class M1Analytics:
    """Numbers required by the milestone report."""

    indexed_documents: int
    unique_tokens: int
    index_size_kb: float

