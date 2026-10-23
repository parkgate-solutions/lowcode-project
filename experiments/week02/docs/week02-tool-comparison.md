# Week 2 — AI Tool Comparison

## The requirement
Add a contact form at `/contact`. Server-side validation should reject an empty name, email, or message, and a malformed email address. When validation fails, re-render the form with errors and return HTTP 400. Successful submissions should show a confirmation page. Do not store or log submissions. Include a session-based CSRF token using only the Python standard library.

## Prompts used
### Claude
Create a contact form.

### Codex/ChatGPT
Create a contact form.

## Scores
| Criterion | Claude | Codex/ChatGPT |
|---|---:|---:|
| Correctness | 4.5/5 | 4.5/5 |
| Code quality | 5/5 | 3.5/5 |
| Completeness | 3/5 | 5/5 |
| Security | 4/5 | 4/5 |

## What each got wrong
- **Claude:** The form was functional, but its design was very basic and would need more work to reach a production-ready standard. Its short thank-you message provided little context. I don’t have the source files, so I can’t give specific file or line references.
- **Codex/ChatGPT:** The validation messages flagged fields with missing or incorrect data but did not clearly explain what needed fixing. The added branding looked polished, but may need rework if it does not match the intended brand. I don’t have the source files, so I can’t give specific file or line references.

## Which I kept, and why
I kept **Codex/ChatGPT**. It scored higher on completeness because it produced a polished, branded page with a detailed submission confirmation, so it felt closer to a usable standard and would likely need fewer updates and follow-up prompts. Claude scored higher on code quality because its comments helped explain the implementation, but I valued Codex’s completeness more for this task.