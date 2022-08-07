# This is a section: Math

This program is planned to support the most basic LaTeX features, you can use inline math with $a + b = c^2$. And this will be the paragraph math:

$$\oint \boldsymbol{B} \cdot d \boldsymbol{A} = 0$$

## This is subsection: Images

You can also insert images with:

![figure](./sample_image.jpeg)

or by:

<img src="./sample_image.jpeg" align="center">

### This is subsubsection: Listings

And code blocks with:

```c
#include <stdio.h>


void say() {
    printf("this is code blocks!");
}


int main() {
    char hello_world[] = "hello world!\n";
    printf(helloworld);

    say();

    return 0;
}
```

#### This is paragraph

Check [example.tex](./example.tex) for the LaTeX rendition of this markdown file. The output of the command is always placed in `./out/`.
