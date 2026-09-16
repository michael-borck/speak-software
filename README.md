# Speak Software

**Programming at the Natural-Language Layer** — a book for people who will never write code by
hand. You describe, an AI agent builds, and the durable human skills — specification,
verification, decomposition, taste — are the curriculum.

Part of the [books.borck.education](https://books.borck.education) series. The hands-on
companion is the [Speak Software labs](https://michael-borck.github.io/programming-labs/).

## Status

First draft complete: 18 chapters, 4 appendices. Fresh-reader pass, print build and cover
pending. See `PROSPECTUS.md` for the plan and the writing queue.

## Build

```bash
quarto render
```

## Checks

```bash
python scripts/check_manuscript.py
python tools/trio_lint.py .
python tools/lab_doctor.py .
```

## Licence

Book content: [CC BY 4.0 International](https://creativecommons.org/licenses/by/4.0/)
([LICENSE-CONTENT.md](LICENSE-CONTENT.md)). Original code examples and accompanying software
(including the tools in `tools/`): [MIT License](https://opensource.org/licenses/MIT)
([LICENSE-CODE.md](LICENSE-CODE.md)). See [LICENSE](LICENSE) for scope.

Separately credited third-party material retains its stated terms.
