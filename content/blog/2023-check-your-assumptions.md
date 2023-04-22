+++
date = "2023-04-22T22:05:40+02:00"
title = "Check Your Assumptions"
+++

In November of last year I noticed that the time it took to process inputs in Ride was way too high, almost a full second between each key input and for a text editor that's unbearable. I tried to tweak the event handling but nothing helped and lost motivation, put the project on ice and started working on other things.

About 3 weeks ago the motivation came back and I started hacking and refactoring on the code to support multiple "backends" for rendering and handling input. Currently it's using OpenGL but I previously had both a wxWidgets and a software renderer backend so it was "only" a matter of bringing them back from the depths of the git history.

Today I got parts of the software rendering working and when testing the samples to make sure the software renderings is working as expected, to my surprise the OpenGL samples weren't lagging. It turns out it wasn't the input code that was the culprit, it was the rendering code.

Armed with RenderDoc after about 15 minutes I had decreased the events from 12 000 to 600, which is still too many, but now the GUI is snappy again.

