+++
date = "2017-07-23T14:31:24+02:00"
title = "Restarting Alsa"
tags = ["linux", "ubuntu"]
+++
Sometimes after I wake up my computer after a hibernate I notice that sound is not playing. A simple fix for this seems to be to restart alsa:

```shell
$ pulseaudio -k && sudo alsa force-reload
```

Found on [Stack overflow](https://askubuntu.com/a/230893)
