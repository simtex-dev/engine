# Rationale

As echoed by Linus Torvalds:

> Software is like sex, it's better when it's free

This program is created with goal of simplifying the writing of assignments in latex by converting markdown language into latex. This program do not intend to replace latex, as well as not to compete with [pandoc](https://pandoc.org/), which provides a fully featured latex conversion. If it does not meant to replace latex, and if pandoc exists, then why this program?

One of the main reason is because latex is antithesis to beauty, as given by a feedback on my post by redditor [u/ArmaniPlantainBlocks](https://www.reddit.com/user/ArmaniPlantainBlocks/) "!*To be fair, Latex is the antithesis of elegance. It's clunky, ugly, messy amd verbose. And more than lightly annotated text can be unreadable. It's a horrid format to work in.!*", which holds true to a certain degree. Pandoc on the other hand, creates a more scary and clunky conversion, albeit the output when compiled to PDF looks good, however can still make latex looks scary and undesirable for use, especially for new users. Thus the program may serve as soft introduction to latex by producing a simple but functional and beautiful output based on user's preference, as well as for people in hurry that can't simply write in latex in some cases.

The program supports **various features**, not __all__ of latex, in fact it allows cross utilization of latex commands in to the input file, as of the current version the program supports:

1. No enumerate yet, so this one is not enumerate.

2. Math mode, inline math, and as for paragraph math, it automatically infers whether to use `equation` or `align`

3. Inline code using `texttt{}`, and code blocks via `lstlisting`.

4. "Smart quotes".

5. Figures.

6. Hyperlinks.

7. Sections, subsections, all way upto paragraph.

8. And as already demonstrated, block quotes.

\newpage

# This is a section: Math

> It is my conviction that pure mathematical construction enables us to discover
> the concepts and laws connecting them which helps us in understanding of nature... .
> In a certain sense, therefore I hold it true, that pure thought
> can grasp reality as ancient dreamed.

The math can be used in number of ways, one is inline math, for example Einstein's equation: $E = mc^2$, paragraph math is also supported either via `equation`:

$$\oint \boldsymbol{B} \cdot d \boldsymbol{A} = 0$$

or `align`:

$$
\sum_{i} \vec{B_{i}} \cdot \vec{\ell_{i}} = \mu_{0} \bigg(I + \varepsilon_{0} \frac{\Delta E \cdot A}{\Delta t} \bigg)
\sum_{i} \vec{E_{i}} \cdot \vec{\ell_{i}} = - \frac{\Delta B \cdot A}{\Delta t}
\sum_{i} E_{i} \cdot A_{i} = \frac{Q}{\varepsilon_{0}}
\sum_{i} B_{i} \cdot A_{i} = 0
$$

## This is subsection: Images

Images can be inserted with^^The first one is in codeblocks using lstlisting, thus not parsed, this is not footnote anyway^^:

```
![figure](./sample_image.jpeg)
```

![figure](./sample_image.jpeg)

### This is subsubsection: Listings

The !*code blocks!* below presents the source code of the "converted" markdown file, which was generated using the one command: `simtex -b -i="examples/1/hello.md" -T="Hello Simtex!" -of="examples/1" -f="hello.tex" -a="iaacornus" -d="August 15, 2552`:

```
# Rationale

As echoed by Linus Torvalds:

> Software is like sex, it's better when it's free

This program is created with goal of simplifying the writing of assignments in latex by converting markdown language into latex. This program do not intend to replace latex, as well as not to compete with [pandoc](https://pandoc.org/), which provides a fully featured latex conversion. If it does not meant to replace latex, and if pandoc exists, then why this program?

One of the main reason is because latex is antithesis to beauty, as given by a feedback on my post by redditor [u/ArmaniPlantainBlocks](https://www.reddit.com/user/ArmaniPlantainBlocks/) "!*To be fair, Latex is the antithesis of elegance. It's clunky, ugly, messy amd verbose. And more than lightly annotated text can be unreadable. It's a horrid format to work in.!*", which holds true to a certain degree. Pandoc on the other hand, creates a more scary and clunky conversion, albeit the output when compiled to PDF looks good, however can still make latex looks scary and undesirable for use, especially for new users. Thus the program may serve as soft introduction to latex by producing a simple but functional and beautiful output based on user's preference, as well as for people in hurry that can't simply write in latex in some cases.

The program supports **various features**, not __all__ of latex, in fact it allows cross utilization of latex commands in to the input file, as of the current version the program supports:

1. No enumerate yet, so this one is not enumerate.

2. Math mode, inline math, and as for paragraph math, it automatically infers whether to use `equation` or `align`

3. Inline code using `texttt{}`, and code blocks via `lstlisting`.

4. "Smart quotes".

5. Figures.

6. Hyperlinks.

7. Sections, subsections, all way upto paragraph.

8. And as already demonstrated, block quotes.

\newpage

# This is a section: Math

> It is my conviction that pure mathematical construction enables us to discover
> the concepts and laws connecting them which helps us in understanding of nature... .
> In a certain sense, therefore I hold it true, that pure thought
> can grasp reality as ancient dreamed.

The math can be used in number of ways, one is inline math, for example Einstein's equation: $E = mc^2$, paragraph math is also supported either via `equation`:

$$\oint \boldsymbol{B} \cdot d \boldsymbol{A} = 0$$

or `align`:

$$
\sum_{i} \vec{B_{i}} \cdot \vec{\ell_{i}} = \mu_{0} \bigg(I + \varepsilon_{0} \frac{\Delta E \cdot A}{\Delta t} \bigg)
\sum_{i} \vec{E_{i}} \cdot \vec{\ell_{i}} = - \frac{\Delta B \cdot A}{\Delta t}
\sum_{i} E_{i} \cdot A_{i} = \frac{Q}{\varepsilon_{0}}
\sum_{i} B_{i} \cdot A_{i} = 0
$$

## This is subsection: Images

Images can be inserted with^^The first one is in codeblocks using lstlisting, thus not parsed, this is not footnote anyway^^:

\`\`\`
![figure](./sample_image.jpeg)
\`\`\`

![figure](./sample_image.jpeg)

### This is subsubsection: Listings

The !*code blocks!* below presents the source code of the "converted" markdown file:

\`\`\`
[REDACTED TO AVOID RECURSION]
\`\`\`

#### This is paragraph

Check [example.tex](./example.tex) for the **LaTeX**, rendition of this markdown file. Since the program is configured via JSON file, the user can modify the behavior of the program in multitude of ways, this includes defining or giving a default value for arguments of the document for easier conversion. Check [simtex.json](https://github.com/iaacornus/simtex/blob/devel/examples/config/simtex.json).

```

#### This is paragraph

Check [example.tex](./example.tex) for the **LaTeX**, rendition of this markdown file. Since the program is configured via JSON file, the user can modify the behavior of the program in multitude of ways, this includes defining or giving a default value for arguments of the document for easier conversion. Check [simtex.json](https://github.com/iaacornus/simtex/blob/devel/examples/config/simtex.json).
