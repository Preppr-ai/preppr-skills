# Preppr Skills

Open, portable AI skills from [Preppr](https://www.preppr.ai) for emergency
management and business continuity. Each skill is a folder of instructions that teaches an AI
assistant how to run one of Preppr's guided workflows, step by step. They use
the [Agent Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
open format, so the same folder works in **Claude**, **GitHub Copilot**,
**Gemini** and **ChatGPT / Codex**. No Preppr account is needed.

There are six skills today. One pre-scripts public alert and warning templates.
Five walk through FEMA planning and assessment work: a risk assessment, a
THIRA, an SPR, a hazard mitigation plan, and a CPG 101 review of an Emergency
Operations Plan. Each one follows a step-by-step protocol, works from the
documents you paste in, pauses for your decisions, and marks missing data as a
gap instead of inventing it.

## Skills

| Skill | What it does |
| --- | --- |
| [`skills/preparedness-alert-warning-templates/`](skills/preparedness-alert-warning-templates/) | Nine-phase guided workflow that produces a per-platform table of alert templates, plus UPDATE and THREAT HAS PASSED follow-ups. |
| [`skills/fema-risk-assessment/`](skills/fema-risk-assessment/) | FEMA IS-393 / 386-2 four-step risk assessment: hazard profiles, asset inventory, loss estimates and a composite risk ranking for an HMP, EOP or THIRA. |
| [`skills/fema-thira/`](skills/fema-thira/) | CPG 201 three-step THIRA: threats and hazards of concern, standardized impacts, and capability targets ready for a community THIRA submission. |
| [`skills/fema-spr/`](skills/fema-spr/) | Stakeholder Preparedness Review: rates current capability against THIRA targets, POETE root causes, sustainment vs. building needs, and grant alignment. |
| [`skills/fema-hazard-mitigation-plan/`](skills/fema-hazard-mitigation-plan/) | Hazard Mitigation Plan builder under 44 CFR 201.6: goals and objectives, mitigation actions in the six FEMA categories, implementation strategy, planning-process record. |
| [`skills/cpg-101-plan-evaluation/`](skills/cpg-101-plan-evaluation/) | Evaluates an Emergency Operations Plan against CPG 101: compliance gaps, missing elements and improvements, with citations. |

The FEMA skills chain: risk assessment feeds the hazard mitigation plan, and
the THIRA feeds the SPR. Each skill tells you when it needs a sibling's output
and accepts a pasted document instead.

Each skill folder contains:

- `SKILL.md` - the skill (YAML frontmatter plus instructions); this is what every tool reads
- `references/` - the protocol the assistant follows (`protocol.json` for the alert skill, `protocol.md` for the others) and `attribution.md` with license, sources and version notes
- `agents/openai.yaml` - optional display metadata for Codex and ChatGPT
- `chatgpt/custom-gpt-instructions.md` - for a ChatGPT Custom GPT (no Codex needed)
- `gemini/gem-instructions.md` - for a Gemini Gem in the Gemini app
- `copilot/*.agent.md` - a GitHub Copilot custom agent, for people who prefer agents to skills

## Where each tool looks for skills

| Tool | Your user profile | This project only | Invoke |
| --- | --- | --- | --- |
| Claude Code | `~/.claude/skills/` | `.claude/skills/` | `/preparedness-alert-warning-templates` or just ask |
| GitHub Copilot (CLI, VS Code) | `~/.copilot/skills/` or `~/.agents/skills/` | `.github/skills/`, `.claude/skills/` or `.agents/skills/` | `/preparedness-alert-warning-templates` or just ask |
| Gemini CLI | `~/.gemini/skills/` or `~/.agents/skills/` | `.gemini/skills/` or `.agents/skills/` | just ask; `/skills list` to check |
| OpenAI Codex (CLI, IDE) and ChatGPT desktop | `~/.agents/skills/` | `.agents/skills/` | `$preparedness-alert-warning-templates` or `@` in ChatGPT |

A single `.agents/skills/` folder in a project is read by Copilot, Gemini CLI
and Codex at once.

## Install

### The quick way (any tool)

```bash
git clone https://github.com/Preppr-ai/preppr-skills.git
cd preppr-skills
sh skills/install.sh claude                       # or copilot, gemini, codex, all
sh skills/install.sh codex --project              # into ./.agents/skills of the current project
sh skills/install.sh all fema-thira               # any skill folder name; default is the alert skill
```

The installer only copies the skill folder to the directory in the table above.

The examples below use `fema-thira`; swap in any skill folder name.

### Claude

- **Claude.ai:** zip a skill folder, for example `skills/fema-thira/` with
  `SKILL.md` at its top level, or download its zip from
  [Releases](../../releases). Then open **Settings > Capabilities > Skills >
  Upload skill**. Start a chat and describe the work, for example "Help me
  build our THIRA."
- **Claude Code:** `sh skills/install.sh claude fema-thira`, then type
  `/fema-thira` or describe what you need.
- **Claude API:** upload the zip through `/v1/skills` and pass the returned
  skill id in `container.skills` on your Messages request. See the
  [Agent Skills overview](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview).

### GitHub Copilot

- **Skill (recommended):** `sh skills/install.sh copilot fema-thira` for
  yourself, or add `--project` to put it in a repository under
  `.github/skills/`. Copilot picks it up from your prompt, or type
  `/fema-thira`. Run `/skills list` in Copilot CLI to confirm it was found.
  See [Adding agent skills for GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills).
- **Custom agent (alternative):** copy the skill's `copilot/*.agent.md` into
  `.github/agents/` and keep the skill folder in the repository so the agent
  can read its `references/`. Select the agent in Copilot Chat and type
  `Start`.

### Gemini

- **Gemini CLI:** `gemini skills install https://github.com/Preppr-ai/preppr-skills`
  installs from this repository, or `sh skills/install.sh gemini fema-thira`
  copies one folder into `~/.gemini/skills/`. Then describe what you need;
  `/skills list` shows what is loaded. See
  [Gemini CLI Agent Skills](https://geminicli.com/docs/cli/skills).
- **Gemini app (Gem):** follow the skill's `gemini/gem-instructions.md`:
  create a Gem, upload the file in `references/` it names as knowledge, paste
  the instructions, type `Start`.

### ChatGPT and OpenAI Codex

- **Codex CLI or IDE extension:** `sh skills/install.sh codex fema-thira`,
  then type `$fema-thira` or run `/skills`. Each skill's `agents/openai.yaml`
  provides its display name and description. See
  [Build skills](https://learn.chatgpt.com/docs/build-skills).
- **ChatGPT desktop app:** install the same way; the skill appears under
  **Skills** in the sidebar and can be chosen with `@`.
- **Custom GPT (web, no install):** follow the skill's
  `chatgpt/custom-gpt-instructions.md`: create a GPT, upload the file in
  `references/` it names as knowledge, paste the instructions, add the
  conversation starter `Start`.

## What to expect

Every skill starts by asking for the documents it needs, then works through its
protocol one step at a time, stopping at each decision point for your answer.
It delivers one continuous document you can copy into your own plan or
submission, and suggests the sibling skill to run next where one applies.

| Ask your assistant | Skill that runs | You get |
| --- | --- | --- |
| "Pre-script an emergency alert for a chemical release at the rail yard." | `preparedness-alert-warning-templates` | A table of alert templates for each platform you use, plus UPDATE and THREAT HAS PASSED follow-ups. |
| "Run a FEMA risk assessment for our county." | `fema-risk-assessment` | Hazard profiles, an asset inventory, loss estimates and a composite risk ranking. |
| "Build our THIRA." | `fema-thira` | Threat and hazard scenarios, standardized impacts and capability targets. |
| "Rate our capabilities against the THIRA targets." | `fema-spr` | Capability gaps by POETE area, sustainment vs. building needs and grant alignment. |
| "Update our hazard mitigation plan." | `fema-hazard-mitigation-plan` | Goals and objectives, mitigation actions, an implementation strategy and a planning-process record. |
| "Does our EOP meet CPG 101?" | `cpg-101-plan-evaluation` | Compliance findings with citations, priority recommendations and an implementation roadmap. |

The skills chain the way the FEMA process does: the risk assessment feeds the
hazard mitigation plan, and the THIRA feeds the SPR. If you already have the
earlier document, paste it instead of running the earlier skill.

Use a long-context reasoning model. The alert protocol alone is about 43,000
tokens, and full plans and annexes add up quickly; for long plans, share the
basic plan first and then one annex at a time.

Everything a skill produces is a draft. Alert templates must be approved by a
qualified alerting official, and plans and assessments by the responsible
planner, before use. Any confidence or priority ratings the model gives are
its own judgment, not a measurement.

## Preppr users

If you have a Preppr account, these skills are also built into **Ask Preppr**
(the Skills panel) and are available to any AI assistant connected through the
Preppr MCP server (`list_skills` and `get_skill`), with your organization's
documents and profile as context.

## Go further with Preppr

These skills run on whatever you paste into the chat. [Preppr](https://www.preppr.ai)
runs the same skills against your own plans, SOPs and after-action reports,
keeps the outputs in a Knowledge Base, and adds the rest of the preparedness
cycle: THIRA and SPR, hazard mitigation plans, CPG 101 plan evaluation, HSEEP
exercise design and evaluation products, simulations and open-source
intelligence. Start an All Access free trial at
https://www.preppr.ai/getstarted.

## License

The skill content and protocols are licensed under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) by Preparedness
Innovations, Inc (dba Preppr.ai). See [LICENSE.md](LICENSE.md). Third-party
sources, including the Warning Lexicon (CC BY 4.0), are cited in each skill's
`references/attribution.md`. Keep the attribution and share adaptations under
the same license.

## Contributing

Issues and pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).
