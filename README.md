# Preppr Skills

Open, portable AI skills from [Preppr](https://www.preppr.ai) for emergency
management. Each skill is a folder of instructions that teaches an AI
assistant how to run one of Preppr's guided workflows, step by step. They use
the [Agent Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
open format, so the same folder works in **Claude**, **GitHub Copilot**,
**Gemini** and **ChatGPT / Codex**. No Preppr account is needed.

The first skill, **Preparedness Alert & Warning Templates**, lets an emergency
manager pre-script a library of compliant public alert templates for IPAWS and
Wireless Emergency Alerts (90 and 360 characters), mass-notification text, email
and voice, X, and other social media. It covers Imminent Threat, Public Safety,
AMBER, Missing Person and Developing Situation alerts, draws on a
research-backed Warning Lexicon, and runs a confidence-scored compliance check
before anything is generated.

## Skills

| Skill | What it does |
| --- | --- |
| [`skills/preparedness-alert-warning-templates/`](skills/preparedness-alert-warning-templates/) | Nine-phase guided workflow that produces a per-platform table of alert templates, plus UPDATE and THREAT HAS PASSED follow-ups. |

Each skill folder contains:

- `SKILL.md` - the skill (YAML frontmatter plus instructions); this is what every tool reads
- `references/protocol.json` - the full protocol the assistant follows
- `references/attribution.md` - license, third-party citations and version notes
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
sh skills/install.sh claude      # or copilot, gemini, codex, all
sh skills/install.sh codex --project   # into ./.agents/skills of the current project
```

The installer only copies the skill folder to the directory in the table above.

### Claude

- **Claude.ai:** zip `skills/preparedness-alert-warning-templates/` (with
  `SKILL.md` at its top level) or download the zip from
  [Releases](../../releases), then open **Settings > Capabilities > Skills >
  Upload skill**. Start a chat and ask, for example, "Help me write a WEA
  template for a boil water advisory."
- **Claude Code:** `sh skills/install.sh claude`, then type
  `/preparedness-alert-warning-templates` or describe the alert you need.
- **Claude API:** upload the zip through `/v1/skills` and pass the returned
  skill id in `container.skills` on your Messages request. See the
  [Agent Skills overview](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview).

### GitHub Copilot

- **Skill (recommended):** `sh skills/install.sh copilot` for yourself, or
  `sh skills/install.sh copilot --project` to add it to a repository under
  `.github/skills/`. Copilot picks it up from your prompt, or type
  `/preparedness-alert-warning-templates`. Run `/skills list` in Copilot CLI
  to confirm it was found. See
  [Adding agent skills for GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills).
- **Custom agent (alternative):** copy
  `skills/preparedness-alert-warning-templates/copilot/preparedness-alert-warning-templates.agent.md`
  into `.github/agents/` and keep the skill folder in the repository so the
  agent can read `references/protocol.json`. Select the agent in Copilot Chat
  and type `Start`.

### Gemini

- **Gemini CLI:** `gemini skills install https://github.com/Preppr-ai/preppr-skills`
  installs from this repository, or `sh skills/install.sh gemini` copies the
  folder into `~/.gemini/skills/`. Then just describe the alert you need;
  `/skills list` shows what is loaded. See
  [Gemini CLI Agent Skills](https://geminicli.com/docs/cli/skills).
- **Gemini app (Gem):** follow
  `skills/preparedness-alert-warning-templates/gemini/gem-instructions.md`:
  create a Gem, upload `references/protocol.json` as knowledge, paste the
  instructions, type `Start`.

### ChatGPT and OpenAI Codex

- **Codex CLI or IDE extension:** `sh skills/install.sh codex`, then type
  `$preparedness-alert-warning-templates` or run `/skills`. The
  `agents/openai.yaml` file provides the display name and description. See
  [Build skills](https://learn.chatgpt.com/docs/build-skills).
- **ChatGPT desktop app:** install the same way; the skill appears under
  **Skills** in the sidebar and can be chosen with `@`.
- **Custom GPT (web, no install):** follow
  `skills/preparedness-alert-warning-templates/chatgpt/custom-gpt-instructions.md`:
  create a GPT, upload `references/protocol.json` as knowledge, paste the
  instructions, add the conversation starter `Start`.

## What to expect

> **You:** Pre-script an emergency alert for a chemical release at the rail
> yard on the east side of town.
>
> **Assistant:** Phase 1 of 9: Onboarding | Step 1 of 2 ... To continue,
> please type 'I AGREE' ...

The assistant walks through platform selection, languages and audiences, alert
type, information collection, a compliance check, and then delivers a table
with one row per platform you selected, each with a self-assessed compliance
confidence and notes. It then offers UPDATE and THREAT HAS PASSED follow-up
templates.

A long-context reasoning model (200,000 tokens or more) is recommended. The
protocol itself is about 43,000 tokens.

All generated templates must be reviewed and approved by a qualified alerting
official before use. Confidence percentages are self-assessed by the model and
are a relative quality signal, not a measurement.

## Preppr users

If you have a Preppr account, these skills are also built into **Ask Preppr**
(the Skills panel) and are available to any AI assistant connected through the
Preppr MCP server (`list_skills` and `get_skill`), with your organization's
documents and profile as context.

## License

The skill content and protocols are licensed under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) by Preparedness
Innovations, Inc (dba Preppr.ai). See [LICENSE.md](LICENSE.md). Third-party
sources, including the Warning Lexicon (CC BY 4.0), are cited in each skill's
`references/attribution.md`. Keep the attribution and share adaptations under
the same license.

## Contributing

Issues and pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).
