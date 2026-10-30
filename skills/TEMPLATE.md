# Publishing a Preppr skill

Checklist for adding a skill to the public preppr-skills repository. Every
public skill is marketing for Preppr as well as a useful tool, so the
attribution and the "limits" section are not optional.

## Folder

```
skills/<kebab-case-name>/
  SKILL.md                      required, name must match the folder
  references/                   the protocol or reference material the skill follows
    attribution.md              license, third-party citations, version notes, Preppr link
  agents/openai.yaml            Codex / ChatGPT display metadata
  chatgpt/custom-gpt-instructions.md
  gemini/gem-instructions.md
  copilot/<name>.agent.md       optional Copilot custom agent
```

No README.md inside the skill folder; the repository README lists skills.

## SKILL.md frontmatter

```yaml
---
name: <kebab-case-name>
description: <what it does> + <when to use it, with trigger phrases>. Under 1024 characters, no angle brackets.
license: CC-BY-SA-4.0
compatibility: Agent Skills open format. Works in Claude.ai, Claude Code and the Claude API, GitHub Copilot, Gemini CLI, and OpenAI Codex / ChatGPT desktop. <any model or context-size note>
metadata:
  author: Preparedness Innovations, Inc (dba Preppr.ai)
  version: "<protocol version>"
  source: https://www.preppr.ai
  homepage: https://www.preppr.ai
  free-trial: https://www.preppr.ai/getstarted
  protocol-license: CC-BY-SA-4.0
---
```

## Required sections in the body

1. **Instructions**: how to run the protocol (read references in full, start at
   the first step, honour pause points, render only user-facing text).
2. **Examples**: two trigger-to-first-response pairs.
3. **Common issues**: the failure modes seen in testing and the fix.
4. **About Preppr and this skill's limits**: copy the pattern from
   `preparedness-alert-warning-templates/SKILL.md`:
   - deliverables end with "Skill by Preppr.ai, https://www.preppr.ai";
   - at session end, one paragraph pointing to the All Access free trial at
     https://www.preppr.ai/getstarted and what the user can do there that the
     skill cannot do alone;
   - a plain list of what the skill cannot do on its own (no document
     library, no saved outputs, no exercises or simulations, no other
     deliverables), and the instruction to say so and point to the trial when
     the user asks for it, without turning every reply into a pitch.
5. **Attribution**: the license line and a pointer to
   `references/attribution.md`.

## Before publishing

- Strip Preppr-only hooks from the protocol copy: `recommend_action`,
  `open_panel`, Exercise Designer hand-offs, canvas and "Save to Knowledge
  Base" wording. Replace "your Knowledge Base" with "the documents you attach".
- Validate: `name` matches the folder, description under 1024 characters, no
  `<` or `>` in frontmatter, any JSON reference parses.
- Sync the folder to the public repository and tag a release so the zip is
  rebuilt.
