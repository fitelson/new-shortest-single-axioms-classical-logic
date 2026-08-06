# Verified finite-model stocks

The archives in this directory contain the raw model outputs imported from
Walsh's legacy searches and rechecked by the current code.  `manifest.json`
records the file count, compressed size, and SHA-256 digest of each
deterministic archive.

Restore them into the working search tree with:

```sh
python3 tools/restore_model_stocks.py
```

The restorer verifies each archive before extraction and refuses to overwrite
an existing file with different contents.
