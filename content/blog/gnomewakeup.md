+++
date = "2016-09-18T14:34:04+02:00"
draft = false
title = "Keep your ubuntu-gnome from waking up at random"
tags = ["hibernate", "linux", "ubuntu"]
+++

I have tried using /proc/acpi/wakeup and I've tried looking in /sys/bus/usb/devices/SOMETHING/power/wakeup for devices that will wake up the computer, however I finally fixed my random wakeup problems with a tool called acpitool.

It is really quite simple. First you need to install it, unless you already have it installed:

 ~ sudo apt-get install acpitool

Once it's installed you can list what you can do with it, and to make it works.

~ acpitool --help

Then you can list all your devices (small w)

~ acpitool -w
   Device    S-state      Status   Sysfs node
  ---------------------------------------
  1. SBAZ      S4    *disabled  pci:0000:00:14.2
  2. PS2K      S3    *disabled
  3. PS2M      S3    *disabled
  4. UAR1      S4    *disabled  pnp:00:06
  5. P0PC      S4    *disabled  pci:0000:00:14.4
  6. UHC1      S4    *enabled   pci:0000:00:12.0
  7. UHC2      S4    *enabled   pci:0000:00:12.2
  8. UHC4      S4    *enabled   pci:0000:00:13.2
  23. PE21      S4    *disabled
  24. PE22      S4    *disabled
  25. PE23      S4    *disabled
  26. USB3      S4    *enabled   pci:0000:00:13.0
  27. USB5      S4    *enabled   pci:0000:00:16.0
  28. PWRB      S4    *enabled   platform:PNP0C0C:00

Then it's just a matter of disable all the devices you don't want to wake up the computer (large W).

~ sudo acpitool -W 6

Don't disable everything, then you can't wake the computer again :)

I keep the power button enabled. And have configured the computer to hibernate when it's pressed, giving me a nice symmetry.
