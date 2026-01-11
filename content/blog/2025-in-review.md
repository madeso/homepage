+++
date = "2026-01-05T14:26:44+01:00"
title = "2025 in Review"
tags = ["year-in-review"]
+++

## spotlight
I spent about 2 weeks on spotlight, my hugo blog featuring pretty windows spotlight images. My windows have stopped showing me new images, not sure what's up with that so the contributions have more or less stopped. I should learn about how image processing works and publish it this year.

## Star trek
The year started with me watching star trek TNG and desperately watching the full series of deep space 9 before it was removed from netflix the last 2 to 3 weeks of the year.

## dotgrid
Similarly the year started with me porting 100 rabbits dotgrid to typescript and letting it wait before digging deep and spending 5 weeks in november/december doing the final steps. There are still some things left that I'll hopefully finish in 2026.

## ubiquity
Another thing that I hopefully can finish or at least continue work on is ubiquity, the mozilla not-ai NLP-based command-line/prompt. I liked the deterministic "ai" prompting and the auto complete like suggestions it could provide. Unfortunately my initial attempt on porting it was unsuccessful and I think I need to do another try this year.


## smide/forma
Speaking of AI, I spent about 4 weeks on both smide and forma.

Smide is an exploration and collection of code generators where you write input in one format, say XML and together with a template like mustache you can generate code.

Forma is a typesafe c++ template engine, originally from blaggen and c#, where you compile a template and a pattern and get back a function specifically for that template. This allows you to check for template syntax errors and then generate or not, instead of most/all template engines that don't have that pre-step so syntax errors are generated (and reported) for each generated call.

Neither project has ended up in production.


## poster tester
Poster tester also got some love, I added icons for all requests and added basic support for endpoints that require authorization. While nothing major I still continue to use and find use for it. 

## ride/pony
From a ride perspective the year started great with continued work on pony, the "vs code" version of ride classic, Prototype Of the New Year or pony. Unfortunately I hit a snag when I decided to rewrite all path types so they are either a valid directory or a valid file and I lost momentum and put it on ice. It wasn't until at the very end I grew tired of vs code and little by litte continued the work. I'm currently working on replacing the syntax coloring selection but it is also kinda back on ice since I want to continue work on euphoria/klotter again.

## euph/workbench
The start of the year continued where the previous left and that was replacing codecov and coveralls with something that can be run locally, complete with a badge that can be displayed on the readme. Then I got an error with my clang-tidy warning parser and I decided that I should solve it with unit testing so that's what I did.

On the euphoria side of workbench I fixed clang-tidy warnings and got 100% on function coverage for the base library.

## klotter
Most of the year was spent on klotter. The first month of development I did rendering multiple objects of the same type with different transforms, aka instancing. I learned about linear vs non linear colors and added basic antialiasing support via MSAA. And was troubled by a bug that took a week to find.

## glox
At this time I grew tired of spending a week on tracking down a bug that only was due to a typo and wanted a typesafe Open GL, explicitly where all enum values were valid for all enum types. I spent a few (2) weeks on a typesafe generator that I could use instead of glad and that could turn a week of bug hunting into a 5 second compile error. I called it glox.

Fortunately a helpful soul told me that my error reporter also sent invalid enum values and after fixing that (and some other) errors it became a runtime error. It's still not as good as a compile time error but it's good enough and I can use standard practices instead of spending a few months (at least) on fixing all the compatibility issues that my generator would have.

So I went back to work on klotter.

## more klotter work
What the experience taught me was that RenderDoc is important as is finding information in it fast. So I spent the following week labeling all OpenGL objects so they are readable in RenderDoc. I continued with removing workbench build and just using straight cmake for dependencies with options to disable the labeling when making a dist build.

With that out of the way was adding a initial HDR renderer with bloom and knee support so the bloom/not-bloom transition isn't hard. There is still much to be done, improving the bloom and adding autoexpose but I tabled that for a later day.

At this point in our story we are in september and I realized that I won't be completing the car game and I lost momentum. After a month I had added directional shadows with PCF filtering and upgraded the dear imgui to the latest version but that was kinda it for that year. There is still much to be done, but my goal remains from last year: Make an arcade game before the end of the year.

## visual debug
With the momentum gone I went looking for greener pastures. I rediscovered Sebastian Lagues visual debugger and wanted something similar so I started "porting" that to klotter and started implementing that but never completed it.

## samling
In between klotter work, and around the time that black week/cyber monday hit, I was looking at various deals for assets and wondering what assets I own and the overlap was. So a thought popped up into my mind, what if there was a tool that could tell me that. The answer was samling, a small application where you could add entries and display them. The overlap and merging of collections is still, after 2 weeks, not implemented. Perhaps next year when black week comes back.


## blaggen
One thing I didn't work on, but want to continue on, is blaggen, my static page generator. I've been also thinking about perhaps learning go and see if I can add the compilation step to hugo but I at least want to continue work and at least make it usable. THe compilation step isn't implemented and I know for a fact that I want to change how templates are applied and I come to like how hugo has done it so I probably just going to copy that. Hopefully I can do that this year, let's see.

## altdev and other conservation projects
One thing I didn't work much on was altdev and other conservation projects. I want to publish the altdev and get more eyeballs on it.


## conclusion
Yeah. I didn't finish the arcade game :(
    
So that leaves only my goals:
1. As I just said, I would like to publish an initial version of altdev
2. and as mentioned earlier I would like to at least complete the klotter project and get the renderer done. Hopefully that will also include a arcade racer
3. and complete blaggen of course, if only to demonstrate the USP
4. and finish the spotlight page

