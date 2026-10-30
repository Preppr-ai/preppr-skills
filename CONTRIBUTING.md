# Contributing

Thanks for helping improve Preppr's open skills.

- Open an issue for wording problems, missing hazards or protective actions,
  platform limits that changed, or a skill that misbehaves in a particular
  assistant. Include the assistant and model you used and the step where it
  went wrong.
- Pull requests should change one skill at a time. Keep `SKILL.md` focused on
  how to run the protocol; put detailed content in `references/`.
- Keep `SKILL.md` frontmatter valid: kebab-case `name` matching the folder,
  `description` under 1024 characters that says what the skill does and when
  to use it, no angle brackets.
- Do not edit `references/protocol.json` by hand for formatting only; keep it
  valid JSON and bump the `version` field and the version notes in
  `references/attribution.md` when the protocol changes.
- By contributing you agree your changes are licensed under CC BY-SA 4.0, the
  same license as the repository.
