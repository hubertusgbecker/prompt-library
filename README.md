# Prompt Library

Prompt Library is a curated collection of reusable AI prompts, templates, and patterns you can use to prototype, teach, and productionize AI-driven workflows.

This repository includes:

- Role-based templates: Prompts tailored to expert personas (for example, architects, reviewers, or domain specialists).
- Use-case collections: Structured sequences for common workflows such as requirements generation, design exploration, sequence diagram creation, and refactoring guides.
- Best practices & patterns: Examples and guidance for clarity, traceability, and consistent prompt engineering.
- Versioning & extensibility: Add, adapt, or contribute new prompts to match your team's needs.

Contributions are welcome — open an issue or submit a pull request with ideas or improvements.

## Quick Start (uv)

This project uses [uv](https://github.com/astral-sh/uv) for Python dependency management.

Install uv (one time):
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Create / sync the virtual environment (includes dev tools like pre-commit):
```
uv sync --group dev
```

Run the index builder:
```
uv run python scripts/build_index.py
```

Run all pre-commit hooks manually:
```
uv run pre-commit run --all-files
```

Activate automatic hooks on commit:
```
uv run pre-commit install
```

Regenerate the index before committing if you added or renamed prompt files.

## Contributing

If you have suggestions for new prompts or improvements, please open an issue or submit a pull request. Please include examples and a short rationale for changes.

## Support

For questions, open an issue or contact the repository maintainers via the project's issue tracker.
