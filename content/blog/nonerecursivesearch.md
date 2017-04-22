+++
date = "2016-08-27T13:07:39+02:00"
draft = false
title = "Non recursive file searching in Nautilus"
tags = ["linux", "nautilus", "ubuntu"]
+++

Recursive search is the default in nautilus (search in subfolders), but I prefer type ahead search(only search in current folder).

This is easy to change, but not very obvious. In dconf-editor navigate to org > gnome > nautilus > preferences and set the enable-interactive-search value to what you'd like to use.

http://www.webupd8.org/2014/01/nautilus-type-ahead-find-feature.html
