# Preppr Skills

Open, portable AI skills from [Preppr](https://www.preppr.ai) for emergency
management. Each skill is a folder of instructions that teaches an AI
assistant how to run one of Preppr's guided workflows, step by step. They work
in Claude, ChatGPT and GitHub Copilot, and they need no Preppr account.

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

- `SKILL.md` - the skill in the [Agent Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) open format (YAML frontmatter plus instructions)
- `references/protocol.json` - the full protocol the assistant follows
- `references/attribution.md` - license, third-party citations and version notes
- `chatgpt/custom-gpt-instructions.md` - instructions for a ChatGPT Custom GPT
- `copilot/*.agent.md` - a GitHub Copilot custom agent

## Install

### Claude.ai

1. Download the latest skill zip from [Releases](../../releases), or zip the
   skill folder yourself with `SKILL.md` at its top level.
2. In Claude.ai open **Settings > Capabilities > Skills > Upload skill** and
   upload the zip.
3. Start a chat and ask, for example, "Help me write a WEA template for a boil
   water advisory."

### Claude Code

Copy the skill folder into `~/.claude/skills/` (personal) or your project's
`.claude/skills/` (shared with the repo):

```bash
git clone https://github.com/preppr-ai/preppr-skills.git
cp -r preppr-skills/skills/preparedness-alert-warning-templates ~/.claude/skills/
```

Then type `/preparedness-alert-warning-templates` or describe the alert you
need.

### Claude API

Upload the zipped folder through the `/v1/skills` endpoint and pass the
returned skill id in `container.skills` on your Messages request. See the
[Agent Skills overview](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview).

### ChatGPT (Custom GPT)

1. Create a Custom GPT and open **Configure**.
2. Paste the text below the divider in
   `skills/preparedness-alert-warning-templates/chatgpt/custom-gpt-instructions.md`
   into **Instructions**.
3. Upload `skills/preparedness-alert-warning-templates/references/protocol.json`
   as a **Knowledge** file.
4. Add the conversation starter `Start`.

### GitHub Copilot

1. Copy the skill folder into your repository so `references/protocol.json` is
   in the workspace.
2. Copy `skills/preparedness-alert-warning-templates/copilot/preparedness-alert-warning-templates.agent.md`
   into `.github/agents/`.
3. In Copilot Chat, select the `preparedness-alert-warning-templates` agent and
   type `Start`.

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
