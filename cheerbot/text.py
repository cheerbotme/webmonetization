#!/usr/bin/env python

import colorsys

import time

from sys import exit, argv

try:

    from PIL import Image, ImageDraw, ImageFont

except ImportError:
    
    exit(
        'install pillow mod: sudo pip'
        + ' install pillow'
    )

print( "Unicorn HAT HD: Rainbow Text" )

import unicornhathd

font = (
    '/usr/share/fonts/truetype/freefont'
    + '/FreeSansBold.ttf'
    , 12
)

fontFile, fontSize = font

font = ImageFont.truetype( fontFile, fontSize )

text = argv[ 1 ]

textWidth, textHeight = font.getsize( text )

textHorizontal = 1

textVertical = 2

width, height = unicornhathd.get_shape()

textWidth += width + textHorizontal

image = Image.new(
    'RGB'
    , (
        textWidth
        , max( height, textHeight )
    )
    , ( 0, 0, 0 )
)

draw = ImageDraw.Draw( image )

unicornhathd.rotation( 90 )

unicornhathd.brightness( 1 )

draw.text(
    (
        textHorizontal
        , textVertical
    )
    , text
    , fill = ( 255, 255, 255 )
    , font = font
)

for scroll in range( textWidth - width ):

    for horizontal in range( width ):

        hue = ( horizontal + scroll ) / float( textWidth )

        baseRed, baseGreen, baseBlue = [
            int( n * 255 ) for n in colorsys.hsv_to_rgb(
                hue, 1.0, 1.0
            )
        ]

        for vertical in range( height ):

            pixel = image.getpixel(
                (
                    horizontal + scroll
                    , vertical
                )
            )

            red, green, blue =  [
                float( n / 255.0 ) for n in pixel
            ]

            red = int( baseRed * red )
            green = int( baseGreen * green )
            blue = int( baseBlue * blue )

            unicornhathd.set_pixel(
                width - 1 - horizontal
                , vertical
                , red
                , green
                , blue
            )

    unicornhathd.show()

    time.sleep( 0.04 )

unicornhathd.off()
