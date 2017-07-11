+++
date = "2009-05-13T10:55:57+02:00"
title = "Foobar sorting"
tags = ["from wordpress", "foobar", "music"]
+++

Since some time I’ve been sorting my music collection. Going though my hard-drives and Cd’s finding all music-files and moving them to a common place and with the help of [foobar2000](http://www.foobar2000.org/) place them in a sane directory-structure and keep them there.

Within foobar I sort the artists on the following script. This makes sure that The (International) Noise Conspiracy is among the other artist that begins with I.

    $replace($replace($replace($stripprefix(%artist%),’|’,),'[‘,),'(‘,)

That little script keeps things nice and tidy within foobar, but to sort I use these two massive scripts:

    $if($greater($strstr(ABCDEFGHIJKLMNOPQRSTUVWXYZ,$upper($left($ascii($replace($replace($replace($stripprefix(%artist%),’|’,),'[‘,),'(‘,)),1))),0),$upper($left($ascii($replace($replace($replace($stripprefix(%artist%),’|’,),'[‘,),'(‘,)),1)),Other)$ascii($swapprefix(%artist%))/$ascii(%title%)

and

    $if($greater($strstr(ABCDEFGHIJKLMNOPQRSTUVWXYZ,$upper($left($ascii($replace($replace($replace($stripprefix(%artist%),’|’,),'[‘,),'(‘,)),1))),0),$upper($left($ascii($replace($replace($replace($stripprefix(%artist%),’|’,),'[‘,),'(‘,)),1)),Other)$ascii($swapprefix(%artist%))/$if([%album%],$ascii(%album%)/,)$ascii(%title%)

The first scripts places All My Loving with The Beatles from the album With The Beatles in BBeatles, TheAll My Loving.mp3 while the scrip places it in B/Beatles, The/With The Beatles/All My Loving.mp3. If  a folder is missing the album tag it places it in the same location as the first one.

I posted these scripts here so that I might use them if my backup fails or for others. As the usual disclaimer goes, they are only tested on my music files, and may not work with yours. I am not responsible for what happens to your files.

It should be noted that if you want to copy these and use them. For gods sake make sure the scrips doesn’t contain any white characters such as spaces or newlines, and that you copy the whole script, those spaces really screw up formatting.
