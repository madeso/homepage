+++
date = "2017-10-17T08:58:16+02:00"
title = "Week41"
+++
This week I actually did a little work on t3d. I started on a tile library and
fixed a problem with the mesh loader in euphoria. I loaded the ambient color and
assimp defaulted to a black ambient, but since most models only specify diffuse
I added a option to assume the ambient color is the same as the diffuse color.
