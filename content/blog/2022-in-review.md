+++
date = "2023-01-01T17:19:08+01:00"
title = "2022 in review"
+++

I recently realized that I've been writing my devlog since 2017 but I have never compiled all the devblogs into a longer post starting from today. I'll summarize and write a smallish review of what I've done on all my hobby projects the past year.

## Euphoria
Euphoria is my hobby game engine and to much surprise I did a couple of cool things related to it.

Code wise I've continued to code cleanup (replacing streams with fmt), both warnings and enabled warning-as-errors(with w4/Wall+extra), I also added both a clang-tidy and coverage step on github actions so I can keep the code clean and strive towards a 100% coverage for the core. Added a PCH cut the compilation time by roughly 66%.

Feature wise most user facing would be the "through the lens" [camera movement](https://www.youtube.com/watch?v=oz4HPDra7g0) in the world/level editor t3d and 3d world selection and [item movements](https://www.youtube.com/watch?v=yyyJLmCYUrw).


## Tred
Speaking of euphoria, the next version of euphoria rendering, [tred](https://github.com/madeso/tred) got a cleanup and refactor, and I started added the world concept.

## Fyro
I also got excited about the thought of a simple engine, something like a [pico-8](https://www.lexaloffle.com/pico-8.php) [love2d](https://love2d.org/) mashup and forked the 2d rendering from tred and started removing all 3d and simplifying it and calling it [Fyro](https://github.com/madeso/fyro). This split allowed tred to focus on 3d with 2d and fyro to only focus on 2d. The 2d sample games was moved to fyro.

Currently there is a working snake clone complete with rumble input and local multiplayer. There is also a 2d platformer base complete with pixel perfect collision (inspired by [celeste and towerfall](https://maddythorson.medium.com/celeste-and-towerfall-physics-d24bd2ae0fc5)), tiled loading and camera movement. All this is controlled by a custom scripting language and that brings us to the next project.

## Lox
I read the first part of [crafting interpreters](https://www.craftinginterpreters.com/), implemented my custom version, [still called lox]() and continued adding on it. If I have any new year resolution is that I should read the second chapter and learn about virtual machines, bytecodes and how to optimize the scripting language.

## Workbench
Looping back to work that I did for euphoria, it wouldn't be possible without the [build/workbench](https://github.com/madeso/build) project. This year I came to the realization that python, while nice to work with, doesn't really result in easy to maintain programs when they grow beyond a certain size and my c++ helper scripts, I think, have reached that size.
So in 2022 I have explored 2 different languages: rust and c#. The rust port is further along, and in some ways have more features than the python version and while I like the language and I don't particularly like to read the code and feel like a variable very often always have the wrong type.

So I tried c# now that Linux support isn't a afterthought and I know from work projects that I both like c# and it's libraries. I encountered a roadblock however in that a nop-build is way slower than both c++ and rust, and since I'm integrating it into console applications I mostly tend to do nop builds when developing.

## Clean code
I started reading clean code and wrote a post about the ["first" (second) chapter](https://i.madeso.me/blog/clean-code-chapter-2/). I also read the "second" (third) chapter and wrote a post about it but since then I learned about what some part actually means so I have yet to rewrite the post and publish it. Another resolution: rewrite that blog post!


## Postertester
In between all the c++ and rust I added a few nice to have features to my [postman clone/replacement](https://github.com/madeso/postertester/) and published the repo. There are still some things to be done before releasing 1.0 and calling it feature complete.

## Other tidbits
I joined a gamejam and [created a game](https://github.com/madeso/spelsylt7-val). I would have made a much better game if I didn't get distracted and started writing my own physics engine.

For my text editor [ride](https://github.com/madeso/ride) I realized I could just copy the fyro code and do the rendering with OpenGL. This turns out works great on Linux but on windows it tends to be a bit laggy. I'm still not sure and I wonder if I have this effect with the older renderers and just didn't notice so I slowly started bringing back part of the old structure where I could test out different rendering APIs for freeform application development. It's still a work in progress but something I hope to continue with in 2023.

I watched a part of [talk by Nikita](https://www.youtube.com/watch?v=l1b7Da2DnPo&t=833s) about [alabaster](https://github.com/tonsky/vscode-theme-alabaster) but didn't like the colors so I started work on a [solarized](https://ethanschoonover.com/solarized/) [version](https://github.com/madeso/vscode-theme-alabaster-solarized), but found bugs in VS code and couldn't continue.

After watching both [Star Trek: Voyager](https://www.imdb.com/title/tt0112178/?ref_=fn_al_tt_1) and [Star Trek: Enterprise](https://www.imdb.com/title/tt0244365/?ref_=fn_al_tt_1) I decided I would start from well... the start so I watched [the original series](https://www.imdb.com/title/tt0060028/?ref_=nv_sr_srsg_0). While I wouldn't say the episodes are great there are some really great ones, and probably at one point I'm going to write a blog post about the great episodes so I won't forget what they are.