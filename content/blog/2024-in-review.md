+++
date = "2025-01-06T19:38:24+01:00"
title = "2024 in Review"
tags = ["year-in-review"]
draft = true
+++


## games
Week 02: This week I made a game in 4 hours
Week 10: With the fyro work also semi-started work on a game jam entry, the goal if I continue on it is to work on the game/fyro for a week and publish a magic game. A nice break from work klotter/euphoria work, let's see if I continue on it or go back to my regular projects.
Week 46: I'm really keen on working on the arcade car game.
Week 52: I think one of my new years resolutions will be making and publishing the car game is some way or another.

Week 39: The following 2 weeks is gamejam time so fyro/lox time will be limited
Week 40: This week I started work on my entry for the the kodsnack gamejam
Week 41: This week I didn't do much I started reading open JK code but I spent most of the week learning "hacking for developers". 

## klotter
Week 01: Thie week I completed framebuffer/post proc and adding support for cubemaps and skyboxes to klotter.
Week 02: This week I added a skybox to klotter, installed sonar lint, fixed some of its suggestions and finally made the existing unit tests compile and run
Week 03: This week I added uniform buffer to klotter
Week 04: This week I worked on instancing, it's still not complete but it's getting there
Week 05: This week I mostly just thought about how to integrate Instancing into klotter and how buffers are connected.
Week 06: I also came to the realization that I need to start "fresh" on the instancing so that's what I'll be doing
Week 07: Regarding klotter I basically deleted all my progress and started fresh with a readme like development and wrote the actual usage... and now I just have to implement the few functions so hopefully I won't get stuck in details this time.
Week 18: Next week will continue the klotter project and the final step is to merge the animation notes, perhaps  with some of the vite animation code into the klotter project, but first there is a lot of klotter to be done.
Week 19: This week I cleaned up some sonar lint warnings in klotter
Week 45: This week I slowly started to work on klotter again
Week 46: I was going to get back into rendering but for one reason or another it didn't happen this weekend either. Perhaps next week.
Week 47: Next week, for sure this time, I need to continue on klotter and get instancing working
Week 48: This week I started to get back into klotter and actually upgraded the glad and opengl version to be the latest that my machines support. next week will be the day I implement instancing in klotter, I promise!
Week 49: I haven't completed instancing but wrote a first revision of the user facing api so all I have left is actually implementing it :)
Week 50: Instancing has been pused back a week or so.
Week 51: My goal before the end of the year is to finally complete the instancing.
Week 52: Last week of the year, but still 2-ish more days of completing the instacing API


## krg
Week 06: This week I implemented 2 different versions of a finite state machine.
Week 07: This week I spend to some watching videos about gui development and refactoring my old widget sizer code that I might reuse for the gui system in euphoria.
Week 43: I've mostly been reading code and trying to understand code, upcomming features for world/level building and whatnot. next week should be lots of work on fyro, finally trying to get the collision code working
Week 44: This week I continued on learning about portals
Week 45: This week I continued work on understanding the portal sample

## animation/vita
https://github.com/madeso/vita
Week 11: This week I a animation book and started compiling the base code for that book.
Week 12: This week I continued on reading and cleaning up animation micro engine.
Week 13: I'm about to start reading chapter 9 of 15 and implementing chapter 8 so with any luck the anim project is soon finished and the knowledge from that can be applied to the kloter project... and speaking of klotter, I really should just continue working on it and actually complete a render project once.
Week 14: This week I continued on animation, reading book, reading articles watching talks writing code... all about animation
Week 15: This week I continued reading about animation... not much more to say really :)
Week 16: This week I continued reading about animation and quickly resurected my old "simple" engine from 15 years ago to see how I solved it last time.
Week 17: This week I finished watching the anim talk and I finished reading the Ik part of the animation book. Next week I'll clean up and understand the IK code and cleaning up my animation notes. After that it's back to klotterfinish up rendering so I can implement all of the animation on top of it, but that is further away than next week, so until then...
Week 18: This week I implemented the IK to my vita animation testbed. I think this marks the project as "completed". There still is chapters to be read but I don't think I will implement them, so I started cleaning up my animation notes.
Week 19: This week I continued cleaning up my animation notes

## euphoria/workbench
Week 08: This week I accidentally commited to euphoria repo and for some reason all the builds started failing, so I worked on fixing them, including updating to the latest catch and the latest compiler that is installed on the runners. Next week I'm going to do some basic workbench things to fix more build issues and then 100% focus on klotter ignoring the euph build errors.
Week 09: This week I continued getting euph build working. clang-tidy is taking too long so that's next. I'm planning to extend workbench and run multiple clang-tidy instances. That should hopefully cut down on the analysis time.
Next up is probably replacing the coverage report. I've grown tired of online services and want something that I can run locally. For the "coveralls" experience I should make sure the result generates a badge and it can be viewed in a browser. But this task lays beond the klotter work. I really want to continue working on klotter and finish the instanced rendering task.
Week 10: This week I got clang-tidy running on Github actions and it looks like it's the only big thing left before everything is green again for euph. I started thinking about replacing the coverage displays like coveralls that I'm currently using with something I can run locally.
Week 23: I am also slowly coming to the conclusion that my main engine, euphoria, has 90% yagni in it. I've always added things that I found interesting and was "game like" but it has somewhat become a behemoth without any features to speak of and I'm strongly considering going over the code and yagni/sunsetting/moving most of the code to a legacy folder until I can find a good place for it. It's working as intended but maybe that isn't enough anymore...
Week 47: Countrary to my plans I didn't really do much this week, mostly just some simple extension to the workbench/buidl project to display statistics on the files you're about to commit.
Week 51: Almost end of the year, I didn't work on instancing but I did some big changes in euphoria. I "removed" pretty much everything and started refactoring the base project. I bumped the unbuntu CI builder and with the new linter comes a new list of warnings to fix or silence. When that is done I can start working on the new dear imgui based editor app with undo/redo support, at least until the 3d rendering is "done".

My goal before the end of the year is to finally complete the instancing.
Week 52: Last week of the year, but still 2-ish more days of completing the instacing API. Other than not working on instancing I've been working on cleaning up euphoria for the car game.

This week, last year, I started replacing the depndency on external coverage reports by also publishing the html report.

## lox
Week 10: This week I also restarted fyro/lox and removed the public/private requirement from code. It was pretty easy since everything was required to be public. Initially I wanted to go in a c# direction but I think a typescript direction is better for lox. It should be easier to implement and stay more true to the original language.

## ride
Week 11: I also got some inspiration to write some ride code so I updated its dependencies, added a todo and started thinking about how to get a useful version working.


## blaggen
Week 12: Both blaggen and kloter has entered my mind and might deserve some love/work but we'll see what the comming week will result in
Week 13: This week I did some small fixes in blaggen
Week 41: I atleast managed to upgraded my static page generator to the latest .net lts and started thinking about perhaps completing it.

## genesis3d
Week 19: This week I started refreshing my memory on the old genesis3d(my favorite)
Week 20: This week I continued work on updating the genesis 3d api
Week 21: I also mostly completed the genesis transformation. It didn't contain what I was orignally looking for so I will probably have to expand to include the extensions I was using and I am in luck because I've saved everything :D
Week 22: Genesis is also comming along nicely. Copying the public documentation the doxygen comments I realize that reading detailed comments is nice, even though the comments aren't exactly helping it is sometimes nice having some comments to look at when pulling hair out trying to figure out a problem. I'm not sure if that's a good enough argument in keeping them around but...

## altdev
Week 20: most of the week have been spent on writing a god awful script to download AltDevBlogADay from wayback machine and replacing archive with modern links where it makes sense. There is some small extraction left to be done but I think the next major thing will be merging several mirrors, since apart from being slow apparently wayback also haven't mirrored everything (404 errors happen). It could be that the page was in a bad state when it was mirrored, who knows...
Week 21: This week I continued working on my altdevblog cloner. I started integrating multiple indexings. I currently merge 3 different timestamps but will probably increase to some more as there is still articles I'm missing.
Week 22: This week I continued on altdev, getting really close to having the text of all posts now. Extracting tags and categories is up next.
Week 23: This week I've mostly been working on the altdev cloning. Categories are done and image cloning is almost done. It's been running for a few days nowand getting closer to completion. Downloading many images, especially if there are lots of redirects, 404s and you want to be nice to the server takes time.
Week 24: This week I continued working on the altdev archive. I'm currently in the process of styling the theme and tweaking the markdown output. Next week is copying the images, making sure there are placeholders for the missing images, and starting downloading the comment section.
Week 25: This week I fixed some/most links for my homepage and continued cleaning up the altdev clone.
Week 26: This week I continued work on the altdev archive. I gave up trying to use pandoc and currently use tidy to convert html to xhtml that can then easily be parsed(mostly) using a regular xml structure. The output is about as good as can be expected when the html is kinda broken but the result is far better than what I had with pandoc. A few weeks more and I think I'm done with markdown generation
Week 27: This week I continued on the altdev archive. I converted the last html to markdown yesterday and it's looking fine. Some small manual cleanup remains. Current step is to algorithmically remove duplicates and it basically consists of looking at various duplicates and see if I can detect and fix patterns early on. Then, and hopefully I can start on this before the end of the week, is copying the comment structure to the hugo setup.
Week 28: This week I continued the work on altdevblog
Week 29: This week I continued work on altdev. Although a new todo pops up almost as fast as I can complete them, I feel like it's getting really close to alpha deploy.
Week 30: This week I continued work on altdev. Still only 2 things left before manual work but hopefully theese are the last 2 things...Let's see if that's true next week :/
Week 31: I'm getting closer to publishing the alpha version of altdev. I'm currently merging duplicates and my goal is to be done with it before the end of the next week, but we'll so how that goes
Week 32: This week I continued with the duplicate removal and merging altdev archive to single posts. It's going slower than I wanted but it's progressing at least. Currently I'm adding extensions to exstensionless images.
Week 33:  altdev cleanup but it's been a slow and steady progress.
Week 46: This week I sent another email to Mike Acton about my flipcode clone, hoping this results in a better response than twitter DM (:/)
Week 50: This week I've more or less just worked on cleaning up the altdevblog for a alpha publication, hopefully before xmas. 

## failed documentation system - kdl
Week 22: The final project I worked on this week is actually a new one, one that I found when reading altdev. It's a documentation system and currently most of the work is converting the ruby code to c# and me trying to understand it. Perhaps I'm having second thoughs about doxygen... we'll see what happens and how it turns out in the comming weeks...

Week 48: I also continued on my kdl project, I'm somewhat considering to replace json with kdl in euphoria.

## blender
Week 28: I'm slowing getting closer to finishing the "blender donut" tutorial


## fyro
Week 32: I also restarted work on fyro, making the code cleaner so I can add object/object collision and response.
Week 33: I managed to continue the fyro refactoring and altdev cleanup but it's been a slow and steady progress. Next week will hopefully be more productive.
Week 34: This week I continued working on fyro and refactoring things. Hopefully next week I can start on adding object-object collisions, we'll see.
Week 35: This week I continued work on fyro. I finally completed the code restructuring and stared doing some small changes, now inheritance support inheriting from classes in namespaces, how about that? I did a rough breakdown of object/object collision and what needs to happen before I can actually start writing code for it and that ball will start rolling next week.
Week 36: This week I continued on fyro object/object collision, expanding the script system type information. I'm not sure I'll be able to finish it next week but I'll keep on working on it
2024 37
This week I continued work on the type system. Variables have types but they can't be set from script. Currently printing the argument information for functions crashes and I'm currently working on making sure that doesn't happen.
Week 39: This week I continued on fyro/lox and got printing working.
Week 44: This week I finally got around working on fyro again


## poster tester
Week 38: some work on poster tester
Week 42: This week I did the final fixes on the upgrade to dotnet 8 for postertester

## bookshelf
Week 39: I also revived an old project and converted it to a hugo theme.
Week 40: continued work on booskhelf
Week 43: few minor changes in  bookshelf

## open jk
Week 41: This week I didn't do much I started reading open JK code

# flipcode
Week 45: This week I started converting flipcode to markdown
Week 46: otherwise I mmostly worked on flipcode




## conclusion

Last year I concluded with
> If there is any goal I really want to complete it is that klotter should be complete and integrated back into euphoria with the new and improved entity system and using lox so I can finally start making some basic 3d games using my own engine.

lol

