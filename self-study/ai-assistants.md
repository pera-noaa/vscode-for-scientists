# AI Assistants in VSCode

Honest take: the lab default is **Gemini Code Assist**, which is helpful for boilerplate and explanations but lags Claude / GPT-4 / Copilot on real refactors. There are three upgrade paths depending on your affiliation.

## The default: Gemini Code Assist
**What it is**: Google's coding assistant, ships as the `googlecloudtools.cloudcode` extension. The lab pays for the Gemini Code Assist tier so everyone in the lab has access.

**What it's good at**:
- Inline completions for boilerplate (loops, common patterns).
- `/explain` on legacy code you don't understand — faster than reading 400 lines by hand.
- `/comment` to add docstrings to a function.
- Simple language translations (Python 2 → 3, IDL → Python sketch).

**What it's worse at**:
- Complex multi-file refactors.
- Catching subtle logic bugs.
- Following nuanced instructions consistently.

Treat it as a search-engine-with-context, not a co-author. It's still meaningfully faster than no AI.

## Upgrade path 1: GitHub Copilot Free (everyone)
GitHub Copilot added a **free tier** in late 2024 — available to anyone with a GitHub account. Limits: 2000 code completions and 50 chat messages per month.

That's enough to be a useful supplement to Gemini. Turn it on and use it side-by-side; over time you'll notice which one you reach for more.

To enable:
```
code --install-extension github.copilot
```
Then Cmd+Shift+P → "GitHub Copilot: Sign In".

## Upgrade path 2: GitHub Copilot full (CIRES / CU staff)
Copilot is **free with unlimited usage** for verified students, teachers, and open-source maintainers via the **GitHub Education** program.

**The CIRES half of the lab qualifies through CU Boulder.** Sign up at https://education.github.com/ with:
- Your `colorado.edu` email.
- A proof of affiliation (school ID, recent class enrollment, or letter from your department).

Verification typically takes a few days. Once approved, you get GitHub Pro + full Copilot for free, renewable as long as you remain affiliated.

The NOAA half of the lab doesn't have this path through their `noaa.gov` email, but most NOAA scientists in the lab also have a CIRES appointment or affiliation that qualifies — check.

## Upgrade path 3: bring your own key (anyone)
If you have an Anthropic, OpenAI, or local API key, two open-source VSCode extensions let you use any model:

- **Continue.dev** (`continue.continue`): chat + autocomplete, integrates with the editor cleanly. Pay-per-token via your own API key.
- **Cline** (`saoudrizwan.claude-dev`): agent-style — reads files, edits, runs commands. More powerful but consumes more tokens.

This route is the most flexible:
- You pick the model (Claude 3.5 Sonnet, GPT-4, Llama via Ollama for local, …).
- You see exactly what you spend (a typical day of moderate use is ~$1–2 of Claude).
- No subscription, no eligibility check.

Setup:
```
code --install-extension continue.continue
```
Then open the Continue panel and paste your API key.

## Practical advice
- Turn on **Copilot Free** (everyone) and **Gemini** (lab default) side-by-side. Use them both for a week; one will feel better and you'll naturally gravitate.
- If you're CIRES, apply for **Copilot full** during onboarding — the verification is slow so start early.
- For one-off heavy lifts (a big refactor, a paper-quality explanation of a legacy script), use **BYO-key with Claude** via Continue.dev for that session, then go back to the cheaper default.
- The **`/explain`** command is the killer feature regardless of which model — it's the first thing to try when opening unfamiliar legacy code.

## Anti-patterns
- Don't let AI write code you can't read. If you can't explain back what the completion does in 30 seconds, don't accept it.
- Don't paste data with PII or sensitive results into hosted models without checking your group's data policy.
- Don't over-rely on `/fix` — read the bug yourself first; the AI's "fix" sometimes papers over a deeper problem.
