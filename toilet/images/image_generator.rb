#!/usr/bin/ruby -w

require 'RMagick'
include Magick

white = ImageList.new("tomato_grey.png").first
grey = ImageList.new("tomato_grey2.png").first

#dark_slice = grey.crop SouthWestGravity, 0, 0, 24, 10
#dark_slice.display


(1..12).to_a.each do |size|
  size = size * 2
  dark_slice = grey.crop SouthWestGravity, 0, 0, 0, size unless size == 0
  percent_pomodoro = white.composite(dark_slice, SouthWestGravity, 0, 0, OverCompositeOp)
  percent_pomodoro.write("pomodoro_#{size.to_s}.png")
end
