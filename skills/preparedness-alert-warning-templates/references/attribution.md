# Attribution and licensing

The structure, workflow, agent logic, and original textual content of the
**Preppr Action: Preparedness Alert & Warning Template Generation**
(version 1.004) protocol are the original work of
**Preparedness Innovations, Inc (dba Preppr.ai)** and are licensed under the
[Creative Commons Attribution-ShareAlike 4.0 International License
(CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).

You may share and adapt it, even commercially, with attribution, under the same
license, with no additional restrictions. No warranties are given.

## Incorporated third-party content

- **The Warning Lexicon** (the `warningLexicon` object) is derived from:
  Sutton, J., Vos, S. C., Wood, M. M., & Schneider, M. (2023). _The Warning
  Lexicon: A Multiphased Study to Identify, Design, and Develop Content for
  Warning Messages._ ASCE. DOI: 10.1061/NHREFO.NHENG-1900. Licensed CC BY 4.0.
- **Missing Persons Alert Guidelines** are informed by: Cain, L. B., Sutton, J.,
  Olson, M., Waugh, N., & Bertola, E. (2025). _Missing information: A content
  analysis of U.S. missing persons alerts using the Missing and Endangered
  Persons Message Framework._ Police Practice and Research, 1-27.
  https://doi.org/10.1080/15614263.2025.2530445 . Standard copyright; the
  protocol is an original expression of the ideas, not a copy of the text.
- **Foundational research:** Miller, S. K. (2024). _Emerging Technology in
  Emergency Management: Using generative artificial intelligence (AI) to
  improve emergency messaging_ (Doctoral dissertation, Capitol Technology
  University).

Full acknowledgements: https://www.preppr.ai/legal/acknowledgements

## What changed in v1.004

- Completed the Phase 5 information-collection paths for Public Safety, AMBER,
  Missing Person and Developing Situation alerts.
- Rebuilt Phase 6 (Compliance Check & User Override) with paths A through F.
- Phase 1.6 high-confidence branch now runs Phases 2 through 4 and shows the
  extracted details in Step 5.1 for confirmation.
- New `platformGuidance` section with per-platform character limits and notes.
- Defined the message content order per alert type.
- Lexicon cleanup.

Note: the compliance confidence percentages produced by the protocol are
self-assessed by the model using the `confidenceFramework`; they are not an
external measurement.
