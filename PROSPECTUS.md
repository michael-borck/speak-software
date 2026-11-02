# Speak Software: Prospectus

Date: 2026-09-17. Status: online-edition-ready draft (updated after the
local HTML/PDF/EPUB build pass); fresh-reader pass and the push stage
(chatbot, publication) pending. Cover is in place.
The living labs remain at `programming/programming-labs` (the "Speak
Software" labs: twelve core labs plus three staff-tool labs, all shipped;
Labs 13–15 pair with this book's harness chapters and its `tools/`
reference implementations); this book is the narrative and the
harness the labs deliberately leave out.

## Thesis

Programming has moved up an abstraction level: the newest way to build
software is to describe, direct, and verify (in natural language) while
an agent writes the code. Vibe coding is not the enemy; *unmanaged* vibe
coding is. The developer's job is no longer typing every line. It is
holding the bar as the **mini CEO of a department of one**: a brilliant,
tireless, overconfident intern.

Two source arguments anchor the book:

1. **Boris Cherny (creator of Claude Code, Anthropic) on "slop"**: black-box
   treatment is fine for low-stakes prototypes; production code written by
   AI deserves a *higher* bar than human-written code: met with automated
   guardrails (lint, tests, AI-driven E2E tests, fuzzers, automated
   reviews), not heroics. The developer is a "mini CEO".
2. **The skill-folder architecture (Anthropic Agent Skills)**: the way past
   the "context wall" is not an agentic framework per task. It is folders
   of markdown instructions and scripts that one capable agent reads on
   demand, spawning "thousands of sub-agents" from organised local files.
   The most sophisticated AI orchestration is basic file organisation.

The twelve labs supply the spine: every lab kills one misconception and
installs one habit. The book adds what the labs deliberately leave out:
the why, the harness, the defence against slop, and the management layer.

## Audience and boundaries

Zero prior programming assumed: the reader who will never write code by
hand. Boundary statement for "What this book is not":

- Not *Code Python, Consult AI*: you will not learn Python syntax.
- Not *Converse Python, Partner AI*: you are not pairing with AI. You are
  directing it.
- Not *Ship Python, Orchestrate AI*: you will commission guardrails, not
  hand-write CI configs (though the book shows what to ask for).
- Compared with *Think Python, Direct AI*: same zero-prior reader,
  different interface: Think puts a language under your fingers; this
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

- **Slop-detector starter kit**: one script (ruff + pytest + coverage
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
print edition timing; recommend after content stabilises.

## Writing queue (2026-09-17)

Done: draft complete. All 18 chapters and all 5 appendices.
Tools done: slop-detector kit (`tools/slop_check.py`), evidence-trio
linter (`tools/trio_lint.py`), lab doctor (`tools/lab_doctor.py`),
manuscript checks (`scripts/check_manuscript.py`). Ch 12 gained a
callout on choosing an agent: where instructions live, what the agent
can reach, what the tool conceals.
Done 2026-09-18: labs drift reconciled. The labs repo shipped Labs
13–15 (staff tools pairing with this book's harness chapters); the
preface, conclusion, slop-defence chapter, evidence-trio appendix and
resources now reference them. Added the Model Access appendix
(accounts, subscriptions, tokens, free tiers and brokers, local versus
frontier, provider handover kit) and a Trust Tool cross-reference in
Chapter 8 and the resources.

Decision recorded 2026-09-17: the book names no public skill collections
(Matt Pocock's skills repo, obra/superpowers) and adds no agent-comparison
table. Named repos date within a year or two, and product tables contradict
the book's stated tool-independence (Ch 12, Ch 17). The named path in the
labs stays pi; any CLI agent works. The agent-comparison handout remains
course material (ISYS6014 Module 7), not book content.

Done in the online-edition pass: standard print files, favicon,
acknowledgments and about-author pages, download and DeepWiki links,
and a validated local HTML/PDF/EPUB build with `llm.txt` and RAG
documents. The acknowledgments are factual and generic; the author
still needs to personalise them.

Next, in order: fresh-reader pass (a named person, not yet done), then
the push stage (chatbot update, commit, publish). Print-edition timing
remains an open question for after content stabilises.
Previous decision stands: the kit and trio linter may also become
additions to the labs themselves.
