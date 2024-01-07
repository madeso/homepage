+++
date = "2024-01-06T20:54:16+01:00"
title = "2023 in review"
+++

Another year full of devlogs and another review of what I have achieved and failed to achieve.

## workbench, euphoria, gaf and json

Workbench started out as a repo of various build scripts, but is now a single tool for running all those "scripts". This year I ported everything from rust to c# and scoured my repos for other tools to integrate it into the code base.

One of the big reasons for choosing C# is so that I can use the spectre project to get a nicer cli.
The other big reason is that I use c# as a language for work so I'm very familiar with it. I can also use resharper to clean up the code and do major refactorings, that wasn't really possible with the rust or the python version.

When the code got better I could integrate more tools, like code city, extract data to a word cloud and a "code-age histogram". Some tools use `git` porcelain mode, some parse the doxygen XML output for code understanding.

For euphoria I mostly watched various talks, about localization, AI and entity system that made me realize how to mostly (re) structure my entity system and now I have a rough plan on how to proceed and what features to add (and remove).
I switched to the main workbench branch and started replacing some custom scripts with the new c# based workbench and basically just started fixing the issues it found.

I realized that the goal of my "protobuf" library gaf was way to complex and too big for me to handle so I started replacing the gaf usage in euphoria with just a simple json library (my own). In 2024 I will archive the gaf repo since, as far as I know there are no users and it will not be completed (by me).

## blaggen

How hard can it be to write a static page generator? That is a terrible question for a "create a new project a week" addict like myself. Blaggen is my answer to that "question". I started out using mustache but ended up writing my own template engine that has a few nice features and can "error out" when you use a property that hasn't been registered.

The big USP is adding custom compile steps, so one could compile, run code examples, write unit tests and insert outputs from those runs. I still like the project and want to continue work on it, unless I start adding the USP to hugo.

Currently it's not useful and it's missing hot reload (and file copying) but that's only because I got motivated to work on tred/klotter again. In 2024 I want to either complete or archive it since it's kinda thorn in my side, sitting there waiting...

## tred is dead, long live klotter

I continued work on tred but came to the understanding that tred focused too much on code quality and best practices. While revision system is better than arc for memory handling, focusing on the best allocation strategy and code abstractions while also trying to get a good rendering API with all features turned out to be much and I lost focus on the rendering. So I started work on klotter. The same basic goal as tred, that is> at some point in the future to integrate it into euphoria, but there is now also anti goals of not focusing on allocation and code prettiness so it doesn't end up in the same place as tred.

## ride

I solved the laggy rendering on windows, making the other rendering backends less relevant, since if you only use one backend the other rot and just make the code more complex.

Every time I use another editor like vs code and notice something [I don't like](https://github.com/madeso/vscode-theme-alabaster-solarized/issues/1), I often wonder how much better ride could be for my use case. For 2024 I want to continue the work on ride and perhaps get it to a working state and while it probably won't end up as my daily driver for quite a while I want to be able to use it, at least, for a short time.

## smaller projects and other tidbits

I started porting bosca ceoil to c++ and started work on a vector graphics editor called vecy. I'm not sure I'm going to complete either but a simple vector editor is something I'm missing.

I also started reading the second chapter of [crafting interpreters](https://www.craftinginterpreters.com/) and hopefully in 2024 I can upgrade lox to a much better system.

## conclusion

I did the first review in [2022](https://i.madeso.me/blog/2022-in-review/) so this is the second one.

Looking back: fyro ended up on the ice this year but that's mostly because I just recently started reading the second part of [crafting interpreters](https://www.craftinginterpreters.com/), in 2024 I will continue the work or at least upgrade the interpreter.

I started reading [clean code](https://i.madeso.me/blog/clean-code-chapter-2/) and a resolution for 2023 was to continue reading and rewrite the blog post about that last chapter. That hasn't happened, so I guess I can repeat what I said last year for 2024

> rewrite that blog post!

I also haven't written a blog post about the great episodes of star trek voyager, the original series and the animated series that I wanted to do last year. My star trek marathon took a break in season 1 of star trek the next generation so this year I should really be watching more star trek!

But I did fix the issue in ride and even though tred "died" it served the lessons and the good code I wrote for it have, or will, be merged into euphoria euphoria (hopefully in the near future).

If there is any goal I really want to complete it is that klotter should be complete and integrated back into euphoria with the new and improved entity system and using lox so I can finally start making some basic 3d games using my own engine.

So... lots of stuff to do in 2024
