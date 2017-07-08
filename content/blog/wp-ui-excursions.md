+++
date = "2009-06-25T11:08:13+02:00"
title = "Excursions into the UI"
tags = ["from wordpress"]
+++

I recently read [scarabus’ post regarding guis](http://www.scalari.net/2009/06/25/lessons-in-gui-design/) and I wanted to follow up/ add a few notes of my own. Since scarabus considers blender to have the worst user-interface(ui for short), I’m going to compare it to other similar applications and guess why it might be non-intuitive.

So, beeing picky I have tried several mesh modelers. The imcomplete list is anim8or, google sketchup, misfit model 3d, xsi modtool, blender, art of illusion, truespace and wings 3d. All of them are free and can be found through google. Other applications are 3d studio max and maya.

Out of all the 3d-applications I could get my hands on(the free ones above), only google sketchup, anim8or and milkshape 3d used the standard windows dialog. All the other applications have implemented their own, and they seem to be lacking several features the standard dialog has. Among the features they seem to be skipping are:

* rememberering the previous folder
* user filers (*dog* lists only files with dog in)
* autocompletion, i.e. when I write the folder/file-names the dialog suggests names based on the existing files/folders
* using my customized spcial folders. I’m refering to thoose folders that appear of the left that usually is my computer, my documents etc.
* pasting the folder/file instead of navigating

Like the google search-bar the filebrowser has a simple interface, but [alot of hidden features](http://lifehacker.com/339474/top-10-obscure-google-search-tricks) that you can learn about at your own pace. So to conclude the file-dialog, the clear winner is Sketchup since they went to the extra length of adding a preview to the standard dialog.

Next, and the only other thing that I want cover is the complexity, and since this is such a huge topic I’m going to split it up into a few categories, the first is shortcuts.

According to [wikipedia](http://en.wikipedia.org/wiki/Blender_(software)) blender was/is considered hard to use since some of its commands are only accessible though keyboard-shortcuts. Originally it only had those shortcuts, but since it went open-source a lot of the time spent has actually been spent on making the software more usable for beginners.

Actually when speaking about shortcuts they are really stupid. Sure they are quick, but unless you use them often they are really hard to remember. A better option is perhaps the [return of the command-line](http://www.codinghorror.com/blog/archives/001265.html), like auto cad, vi or launchy/quicksilver.

Then again, the blender interface looks much cleaner than the icon-filled interface of [maya](http://en.wikipedia.org/wiki/File:Maya2009.png) and if I’m not mistaking alot of the time in 3d studio max was spent on scrolling through the list of commands([on the right](http://en.wikipedia.org/wiki/File:3dsmax_2010_800px.png)).From what I’ve heard about the keyboard-shortcut interface design of blender is that it is a steep learning-curve, but once you know the shortcuts, it is faster than both max and maya.

Onwards with custom controls. One reason blender might have gone with the complete custom gui, is that it makes porting easier. First and foremost there is basic compatibility. Radio buttons in main-menus doesn’t exist on the motif platform for example. Then there are the user-interface guidelines, for windows vista this is a 100+ pages document, and for mac ther is the cocoa api that helps you, and I’m guessing implements some other standards that aren’t documented in the ui guidelines. Something a simple as the [OK & Cancel button combinations](http://designlibrary.blinkinteractive.com/2007/11/button-button-w.html) are placed differently on the different OS’s. Windows places the OK to the left, while mac places it to the right. For windows there are even a few documents (10+ pages long) that describe how icons should look. Perspective, details color-scheme and that sort of things.

Blenders solution to this complicated mess is to be completely different, and hence use it’s own ui-conventions, and if we are going to rant on applications that ignores some ui-conventions. Autocad uses space and right-click as accept in most contexts, Maya seems to have thrown out the standard dropdown-context menu for a pie-menu and the handy cmd.exe ignores most common text-commands.

To complete this post on why blender isn’t the worst gui, and as a recap of some sort, I thought it would be a good idea to quickly go through scarabus’ list and compare it to blender.

* left/right mouse buttons are switched – you can change/switch them easily, but given that most of blender’s ui is context click and selecting objects in menus I like the default setting better. This might also be a conscious decision because of touchscreens/pens(wacom) and single-button-mice.
* ctrl-c/ctrl-v doesnt copy/paste. I’ve never copied/pasted in blender but I assume you can change the shortcuts to whatever you want. Then again, what should the default be? A solution might be to have a different default-configuration per platform but that might be hard to maintain.
* common controls have already been discussed in greater deatil above, and to keep a long story short, the big issue is compability. motif doesnt support radio buttons in menus, windows and mac have switched places between ok and cancel so I assume blender took the easy route and made their own gui, like qt and mozilla did.
* there are hover-hints within blender.

Well thats it. I hope you learned something 🙂
