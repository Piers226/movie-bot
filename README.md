python3 -m venv venv
source venv/bin/activate

## Linting

This project uses [Ruff](https://beta.ruff.rs/docs/) for linting.

To run the linter:
```bash
ruff check src
```

Configuration for Ruff is located in `ruff.toml`.