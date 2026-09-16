# Speak Software: Prospectus

Date: 2026-09-16. Status: planning — skeleton, chapter plan and strategy.
The living labs remain at `programming/programming-labs` (the "Speak
Software" labs, 12 labs, all ready); this book is the narrative and the
harness the labs deliberately leave out.

## Thesis

Programming has moved up an abstraction level: the newest way to build
software is to describe, direct, and verify — in natural language — while
an agent writes the code. Vibe coding is not the enemy; *unmanaged* vibe
coding is. The developer's job is no longer typing every line. It is
holding the bar as the **mini CEO of a department of one**: a brilliant,
tireless, overconfident intern.

Two source arguments anchor the book:

1. **Boris Cherny (creator of Claude Code, Anthropic) on "slop"**: black-box
   treatment is fine for low-stakes prototypes; production code written by
   AI deserves a *higher* bar than human-written code — met with automated
   guardrails (lint, tests, AI-driven E2E tests, fuzzers, automated
   reviews), not heroics. The developer is a "mini CEO".
2. **The skill-folder architecture (Anthropic Agent Skills)**: the way past
   the "context wall" is not an agentic framework per task — it is folders
   of markdown instructions and scripts that one capable agent reads on
   demand, spawning "thousands of sub-agents" from organised local files.
   The most sophisticated AI orchestration is basic file organisation.

The twelve labs supply the spine: every lab kills one misconception and
installs one habit. The book adds what the labs deliberately leave out:
the why, the harness, the defence against slop, and the management layer.

## Audience and boundaries

Zero prior programming assumed — the reader who will never write code by
hand. Boundary statement for "What this book is not":

- Not *Code Python, Consult AI*: you will not learn Python syntax.
- Not *Converse Python, Partner AI*: you are not pairing with AI — you are
  directing it.
- Not *Ship Python, Orchestrate AI*: you will commission guardrails, not
  hand-write CI configs (though the book shows what to ask for).
- Compared with *Think Python, Direct AI*: same zero-prior reader,
  different interface — Think puts a language under your fingers; this
  book puts a department at your command. A routing note in the preface
  will help beginners choose.

## Position in the series

Eighth title; web track stays Build Web. Sits beside CND (the
discipline-neutral philosophy) as the second book a non-programmer can
read first. The labs repo stays the living lab host (TAMYMN pattern): the
book narrates the why and the harness; the repo hosts the doing. They
cross-link.

## Sources to cite

- Boris Cherny / Claude Code "What to do about slop?" exchange and the
  mini-CEO guidance (paraphrase; quote sparingly and attribute).
- Anthropic Agent Skills documentation (skill folders, SKILL.md).
- Andrej Karpathy on vibe coding (term origin, early 2025).
- Y Combinator W25 95%-AI-generated statistic (hedged, "reportedly").
- The author's *Conversation, Not Delegation* (2025) for the Conversation
  Loop and VET framework.

## New chapters beyond the labs (the missing harness)

| Chapter | Fills the gap |
|---|---|
| The Slop Question | Frames restrained-vs-vibe, blast radius, black-box threshold; the Cherny argument |
| The Slop Defence | The assembled gate: lint + tests + coverage floor + TODO sweep + diff-size budget + a CI recipe to commission |
| Slop in the Supply Chain | Hallucinated packages (slopsquatting), dependency vetting, licence/attribution, what never to paste |
| The Filing Cabinet | Skill folders: context wall, SKILL.md + scripts, sub-agents on the fly, company-scale organisation |
| The Mini CEO's Staff | Reviewer-agents vs builder-agents, model pinning and upgrade strategy, cost as a constraint |

## Missing tools and harnesses to build or reference

- **Slop-detector starter kit**: one script — ruff + pytest + coverage
  floor + TODO/FIXME count + diff-size budget, readable thresholds.
- **CI recipe per lab**: GitHub Actions the reader commissions from the
  agent (never hand-writes).
- **Evidence-trio linter**: validates SPEC.md / DECISIONS.md / CRITIQUE.md
  exist, are non-empty, and SPEC contains acceptance criteria.
- **Replication Test log**: fill-in template for the spec-sprint record.
- **Lab doctor**: environment pre-flight (agent, git, model credit).
- **Model/version pinning per lab** with expected cost, in RESOURCES.
- **Slop lexicon**: slop, blast radius, black-box threshold, guardrail,
  harness, mini CEO, context wall, skill, sub-agent.

## Publication model

Quarto book in this workspace, standard series pipeline (licence files,
collection licence check, rendered-book validation, source checks).
Formats: HTML primary; PDF/EPUB via the standard print pipeline. The labs
repo keeps its own site; cross-links both ways. Open question for later:
print edition timing — recommend after content stabilises.

## Writing queue (2026-09-16)

Done: skeleton, Ch 1 (Hello, Department of One), Ch 2 (The Slop
Question), Ch 3 (The Demo Illusion), Ch 9 (The Slop Defence — the kit).

Next, in order: Ch 4 (Say What You Mean), Ch 5 (The Checklist It Can't
Charm), Ch 6 (The Flight Recorder), Ch 7 (Teach the Intern), Ch 8 (Trust,
Then Verify), Ch 10 (The Taste Test), Ch 11 (The Last 20%), Ch 12 (The
Filing Cabinet), Ch 13 (Slop in the Supply Chain), Ch 14 (Run the
Department), Ch 15 (The Audit), Ch 16 (Ship Something True), Ch 17 (The
Mini CEO's Staff), Ch 18 (Conclusion), then appendices. Then the tools:
slop-detector kit as a repo file, evidence-trio linter, lab doctor.
Decision made: the kit and trio linter may also become additions to the
labs themselves.
