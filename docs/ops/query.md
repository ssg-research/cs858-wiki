# Operation: Query

**Trigger:** Someone asks a question the wiki should be able to answer (which
papers touch X, what concept Y means in this course, which section a paper sits
in).

## Steps

1. Read `wiki-f26/README.md` to orient (stats, sections, navigation).
2. Find the relevant pages. Match the question's topic against concept
   `description` frontmatter: `grep -h "^description:" wiki-f26/concepts/*.md`. This
   is faster than scanning every page. For which papers use a concept,
   `grep -rl "concepts/<slug>.md" wiki-f26/papers/`.
3. Read the matched concept and paper pages.
4. Answer with citations to wiki pages, as relative Markdown links.
5. Do not invent claims the wiki does not support.
6. If the wiki lacks enough information, say so explicitly. If you answer from
   general knowledge, flag that it did not come from the wiki.

## What the wiki will and will not tell you

The wiki is a *reading companion*. It will tell you what a paper assumes, what
open questions it sits inside, and which course section it belongs to. It will
**not** tell you the paper's findings or results; those live only in the paper,
by design. If a question asks "what did paper X conclude," the honest answer is
"the wiki does not summarize conclusions; read the paper," not a fabricated
summary.
