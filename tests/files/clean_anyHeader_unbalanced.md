# Markdown

## Headers

### ATX

# H1
## H2
### H3
#### H4

### Setext

Header 1
====
Header 1
========
Header 1
============

Header 2
---
Header 2
--------
Header 2
-----------

## Whitespace

This line has four spaces at the end.
This line has two spaces at the end.  
This line has one space at the end.

## Emphasis

**bold**
_italics_
**_bold and italics_**
**_bold and italics_**
**_bold and italics_**
**_bold and italics_**
**_*bold and italics*_**

## Horizontal Rules

--

---

---

---

Header2
-------
NotAHeader
***

---

---
***
___
---

## Links

### Missing

This paragraph has three links. One [missing][], one [referenced][], and one [with id][id].

[referenced]: http://referenced
[id]:         http://id.com
[missing]:    404

Oh yeah, there's one [here][], too.

[here]: http://here.com

### Referenced

You can use [Google][] or [Bing][] to search the internet.

[Google]: http://google.com
[Bing]:   http://bing.com

You can also use [DuckDuckGo][] but I never have.

[DuckDuckGo]: https://duckduckgo.com/

### Images

You can also reference ![images][] as if they were a normal ![link][].

[link]:   http://link.com
[images]: 404

## Lists

### Unordered

- Item 1
- Item 2
    + Item 1.1
    + Item 1.2
    + Item 1.3
        * Item 1.3.1
            - Item 1.3.1.1
            - Item 1.3.1.2
        * Item 1.3.1
- Item 3
    + Item 3.1
- Item 4

- Item 5

    + Item 5.1

    + Item 5.2

### Ordered

1. Item 1
2. Item 2
    1. Item 2.1
    2. Item 2.1
3. Item 3
    1. Item 3.1
        1. Item 3.1.1
        2. Item 3.1.2
            1. Item 3.1.2.1
4. Item 4

5. Item 5

    1. Item 5.1

    2. Item 5.2
