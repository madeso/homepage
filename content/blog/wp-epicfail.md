+++
date = "2009-07-29T11:26:22+02:00"
title = "Epic fail"
tags = ["from wordpress"]
+++

I probably should have posted this earlier, however I been sleeping and sobbing over the fact that I didn’t finish [no more sweden](http://www.nomoresweden.com/) :). A few hours before deadline all tiles in one layer went 3 tiles up, but collision-tiles were still in the same place. I though that was strange so I went to check the map in the [(external) editor](http://mapeditor.org/), and to my horror it didn’t load. No message, no crash nor any exception – just silence.

So the map-editor didn’t want to load my map, some tiles were 3 tiles away(kinda makes platforming hard) and my here, who was going to be a noble knight, looked like a 3-year-old was trying to draw the spaghetti-monster and failed. I gave up.

Next time around I use my own editor that doesn’t require you to exit when loading, doesn’t write a schema link that forces a proper xml-reader to verify it and support external entities and rotated sprites, plus I’m gonna use a library that’s a little bit more stable.

I made the mistake to use sfml.net without prior testing. Turns out that there is a bug in it that makes fonts unusable. I should be a good open-source developer and track that bug down, and let the sfml guys know of it, since they have done such a nice library and are quick with the support/responses on the forums.

Anyway, no more sweden was a fun, despite the fact that I was at work for the most of the time, and I hope to do it again next year, hopefully with a better planned vacation.
