+++
date = "2017-05-18T07:28:24+02:00"
draft = false
title = "A fix for spotify filling up the C: drive"
tags = ["spotify", "windows", "ssd"]
+++

I recently got a notice that my SSD C: drive was getting low on space and after a quick check with WinDirStat I noticed that spoitfy was filling it up with loads of weird files in the AppData\Local\Spotify\Data folder, even after I have moved my cache location.

It turns out the "cached location" is only the saved playlists, and the Data folder is the cached songs that arent in a playlist.

MSchnyder from the [spotify forums](https://community.spotify.com/t5/forums/v3_1/forumtopicpage/board-id/001/thread-id/9733/page/2) found this solutuion:


1. Close spotify
2. Delete the "data" Folder under ...AppData\Local\Spotify....
3. Start CMD as Admin and type: Mklink "C:\Users\%USERNAME%\AppData\Local\Spotify\Data" "E:\Spotify\Data" /D where E:\Spotify\Data is the new Spotify Data folder.

This command creates a Data Folder under Appdata\Local\Spotify which will be redirected to the target Path (here as example: E:\Spotify\Data")

Nice! Now my SSD has plenty of space again.
