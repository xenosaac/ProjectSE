# ICS Search Engine (M1 Skeleton)

Group member(s):
- Isaac Zhang
- Owen Yang
- Kent Ziti
- David Deng

This repository currently contains:
- `main.py`: CLI entry point (implemented)
- `search_engine/`: pipeline/storage skeleton with TODO stubs

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```



## What To Implement Next (M1)

1. In `search_engine/pipeline.py`, implement:
   - document discovery over JSON files
   - robust HTML parsing and token extraction
   - Porter stemming with no stop-word removal
   - term-frequency posting creation
   - streaming partial-index flush + final merge
2. In `search_engine/storage.py`, implement:
   - partial write format
   - merge-friendly on-disk layout
   - final lexicon with byte offsets
   - analytics persistence
3. Keep output file-based for both modes. This matches developer constraints and
   avoids redesign later.

## Notes on Efficiency

- Never load all documents into memory.
- Never keep the entire final inverted index in memory.
- Flush partial index to disk multiple times before merge.
- During retrieval (M2+), seek to term offsets in `index.postings` using
  `index.lexicon` instead of loading everything.
