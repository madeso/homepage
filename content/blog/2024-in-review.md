+++
date = "2025-01-06T19:38:24+01:00"
title = "2024 in Review"
tags = ["year-in-review"]
+++

## games
THe only game I made this year, was a game made in 4 hours for the spelsylt gamejam.

I think one of my new years resolutions will be making and publishing the car game is some way or another.
I'm really keen on working on the arcade car game.

## klotter

The year started strong with implementing framebuffer/post proc, cubemaps, skyboxes and uniform buffers and continued with code cleaning in the end of february but then I just stopped and was stuck on instancing and having some sort of analysis paralysis and ignoring for most of the year before almost completing it before the end.

## learning and planning
Instead of klotter I found other work, I looked into how to implement finite state machines, gui development, portal rendering and worked on reading the jedi knight academy source.

## animation/vita
I read most chapters of a animation book over the course of about 2 months, only skipping the crowd rendering, and that resulted in the mini-engine [vita](https://github.com/madeso/vita). I won't use the code directly in euphoria but it was a good experimentation.

## euphoria/workbench
I did work on workbench, my c# build tool and source code status app, not a major overhaul or anything but I optimized the clang-tidy build and ended the year by starting to replace the external coverage reporter with a workbench one that I can run locally. For euph I upgraded the ubuntu builder and moved most of the code to a legacy folder so I can focus on the car game.

When that is done I can start working on the new dear imgui based editor app with undo/redo support, at least until the 3d rendering is "done".

## blaggen
My static page generator didn't get much love this year, just some small fixes and a upgrade to the latest LTS. I want to complete at some point as it has some cool unique features.

## ride
I think my ride editor will get most of my focus this year. I can remove most of the rust parts and make a generic "vs code" like and "prototype of the new year" is a good name.

## genesis3d
Genesis 3d is a old engine and I stated thinking about the API and how easy it was to use. I spent a month convering the c headers to c++ and added moved the documentation to a doxygen compatible headers. I realized that having some basic api documentation in plain english is kinda nice when trying to figure out why a function fails.

## altdev & flipcode
About 4 months of the year was spent on cloning and converting a old blog called "altdev" from internet archive to hugo. It's close to completion but not yet ready for publication.

I also looked at flipcode. It still is online but the mobile version is pretty bad and it would be nice if it was better.

For some reason I have been thinking much about having a local archive of your favorite (static) webpages.

## blender
I finished both the blender "rite of passage" donut tutorial and the anvil. Hopefully there will be more finished blender products this year.

## fyro & lox
For lox, I remove dthe public/private requirement and moving it in a more typescript direction than the original c# direction. I also started on type information but decided that it would be better to actually continue by making the interpreter into a compiler and vm structure.
The other side of this project was a lot of fyro work and preparing for object-object collision that will be based on the type system, but since that is tabled for later so will the object-object collision.

## bookshelf
I like to read when I'm commuting by train and for this winter season when I'm commuiting I decided to rrevive and an old project and convert it to a hugo theme. This is bookshelf, a book like theme with some sample books that I can read on my train rides.

## conclusion
Last year I concluded with

> If there is any goal I really want to complete it is that klotter should be complete and integrated back into euphoria with the new and improved entity system and using lox so I can finally start making some basic 3d games using my own engine.

lol

Hope this year will be better and more of my predictions/plans will come true.
