+++
date = "2013-08-22T13:42:58+02:00"
title = "Thoughts on the controls"
tags = ["spacehustler", "input"]
+++
I have started implementing the basic controls for both the keyboard and joysticks
and to test everything out I added basic thrust and torque controls, and while this
is really hard to control as each torque requires a counter torque from stopping
to spinning I started thinking. The [WebGL version of lander](http://lanael.free.fr/webgl/hopper.html) and I recall the original
(I still can’t get it to play on my win7 system) let’s you enter the desired orientation
and let a AI controls the torque thrusts. This is a much easier control scheme as you don’t
have to compensate for the rotational adjustments.

Going a step further one could add another AI layer to control the main thruster and let the player use a fps-like control to control the lander. With this control system a couple of issues arise on how the camera, the input display and, most important, the aiming should work, and I’m thinking time and testing will only tell if this is a feasible input system, I believe it’s a good way to testing the AI that will be controlling the enemy landers.
