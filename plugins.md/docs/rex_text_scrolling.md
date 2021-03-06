## Introduction

Scroll content of text.

Icon: [Icons8](https://icons8.com/)

## Links

- [Plugin](https://rexrainbow.github.io/C3RexDoc/repo/rex_text_scrolling.c3addon)

## Dependence

- One of these plugins
    - [official text](https://www.scirra.com/manual/116/text)
    - [official sprite font](https://www.scirra.com/manual/166/sprite-font)
    - [rex_tagtext](rex_tagtext.md)
    - [rex_bbcodetext](rex_bbcodetext.md)
    - [spritefont+](https://www.scirra.com/forum/plugin-spritefont_t91528?)

## Usage

```mermaid
graph TB

ActSetContent["Action:Set content<br>Action:Append content"] --> |Percentage| ActScrollByPercentage["Action:To percentage"]

ActSetContent --> |Line| ActScrollByLines["Action:Next line<br>Action:Previous line<br>Action:To line"]

ActSetContent --> |Page| ActScrollByPages["Action:Next page<br>Action:Previous page<br>Action:To page<br>Condition:Last page"]
```

1. Put this behavior under
    - [official text](https://www.scirra.com/manual/116/text)
    - [official sprite font](https://www.scirra.com/manual/166/sprite-font)
    - [rex_tagtext](rex_tagtext.md)
    - [rex_bbcodetext](rex_bbcodetext.md)
    - [spritefont+](https://www.scirra.com/forum/plugin-spritefont_t91528?)
2. Set content
    - `Action:Set content`
    - `Action:Append content`
    - `Expression:Text` : content of text
    - `Expression:Lines` : string from start line to end line
3. Scroll to
    - Percentage  ([Sample capx]())
        - `Action:To percentage`
    - Line  ([Sample capx](https://1drv.ms/u/s!Am5HlOzVf0kHl2BFdyr2oS-3qmu0))
        - `Action:Next line`
        - `Action:Previous line`
        - `Action:Tto line`
    - Page  ([Sample capx](https://1drv.ms/u/s!Am5HlOzVf0kHl2GYd7NAye5E-kyk))
        - `Action:Next page`
            - [Sample capx]() : [Typing](rex_text_typing.html) text page by page
        - `Action:Previous page`
        - `Action:To page`
        - `Condition:Last page`

- Properties
    - Lines count
        - `Expression:TotalCnt` : total lines
        - `Expression:VisibleCnt` : visible lines in a page
    - Line index
        - `Expression:CurrIndex` : index of current visible line
        - `Expression:CurrLastIndex` : index of current last visible line

!!! warning 
    Don't set text in text object directly.