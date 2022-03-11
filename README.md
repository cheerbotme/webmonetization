# web monetization payment remote 

Using the https://webmonetization.org solution to remote control a raspberry pi with fiat-$ payment.

Basic pixelart functionality for a Raspberry Pi Zero W with a [Pimoroni unicorn hd HAT](https://shop.pimoroni.com/products/unicorn-hat-hd).

<p align="left">

   <img src="https://user-images.githubusercontent.com/3211305/157890344-722240ef-1119-45c7-8320-a64fbb1aa555.png" width="25%">
   
</p>

## how to install cheerbot on Raspberry Pi

Modify this repo's `wpa_supplicant.conf` with your wifi's information. 

Follow the instructions here to flash a Raspberry Pi OS on a SD card:

* `https://www.raspberrypi.com/documentation/computers/getting-started.html#using-raspberry-pi-imager`

When done, select the SD card's `boot` partition: 

* drag/drop this repo's `ssh` into the `boot` partition

* drag/drop the `wpa_supplicant.conf` you modified into the `boot` partition.

Select the SD card's `rootfs` partition and navigate to the `home/pi` folder:

* drag/drop this repo's `cheerbot` folder into the `home/pi` folder

Eject the SD, put it into the Raspberry Pi, plug the power USB into the Raspberry Pi and wait for the Raspberry Pi to boot up. 

When booted, open Terminal in your computer `ctrl+alt+t` and SSH into the Raspberry Pi with `ssh pi@raspberrypi`.

When you have entered the Raspberry Pi with SSH: 

* change the password with `passwd`

* install the unicorn hd HAT dependencies with `curl https://get.pimoroni.com/unicornhathd | bash`

## join the Discord and help buidl cheerbot

https://discord.gg/KXzXR7DVqb
