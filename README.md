# web monetization payment remote 

Using the https://webmonetization.org solution to remote control a raspberry pi with fiat-$ payment.

[MozFest 2022 presentation](https://www.youtube.com/watch?v=gU2WKhQRXQA&list=PLL0gyjXno6ejvzUw1SOfmKHFN6gPNjHfI&index=20).

Basic pixelart functionality for a Raspberry Pi Zero W with a [Pimoroni unicorn hd HAT](https://shop.pimoroni.com/products/unicorn-hat-hd).

Based on [this action plan](https://community.webmonetization.org/bestape/alchemy-cheerbot-mozfest-2022-web-monetization-action-plan-p56) and used by [this MozFest 2022 Emergent Session](https://schedule.mozillafestival.org/session/PRQV3L-1). 

<p align="left">

   <img src="https://user-images.githubusercontent.com/3211305/157890344-722240ef-1119-45c7-8320-a64fbb1aa555.png" width="100%">
   
</p>

## how to install cheerbot on Raspberry Pi

Modify this repo's `wpa_supplicant.conf` with your wifi's information. 

Modify this repo's `cheerbot/index.html` with your [payment pointer](https://esse-dev.github.io/a-web-monetization-story/).

Follow the instructions here to flash a Raspberry Pi OS on a SD card:

* `https://www.raspberrypi.com/documentation/computers/getting-started.html#using-raspberry-pi-imager`

When done, select the SD card's `boot` partition: 

* drag/drop this repo's `ssh` into the `boot` partition

* drag/drop the `wpa_supplicant.conf` you modified into the `boot` partition.

Select the SD card's `rootfs` partition and navigate to the `home/pi` folder:

* drag/drop this repo's `cheerbot` folder into the `home/pi` folder

Eject the SD, put it into the Raspberry Pi, plug the power USB into the Raspberry Pi and wait for the Raspberry Pi to boot up. 

When booted, open Terminal in your computer `ctrl+alt+t` and SSH into the Raspberry Pi with `ssh pi@raspberrypi`.

When you've entered the Raspberry Pi with SSH: 

* change the password with `passwd`;

* install the unicorn hd HAT dependencies with `curl https://get.pimoroni.com/unicornhathd | bash`.

`cd cheerbot` to enter the cheerbot folder.

Run `npm install socket.io` to install socket.io.

Modify `app.js`'s port and url `5571` and `mozfest` default definitions to your preference.

To turn on the server, run `./app.js`.

When the server is on, assuming port and url in `app.js` are unchanged, navigate to the remote control website with `http://YOUR_IP_ADDRESS:5571/mozfest`.

Note that http is used, not https.

See the image above for an example. 

## port forward

You'll have to port forward your router to your Raspberry Pi, which is different for every router.

There's a good chance you can find instructions about how to port foward your router at [https://portforward.com](https://portforward.com/).

To use a url rather than an IP address, change the A-record with your DNS server provider to your IP address.

## join the Discord and help buidl cheerbot!

https://discord.gg/KXzXR7DVqb
