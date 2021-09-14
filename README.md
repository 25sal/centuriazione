# centuriazione
##downloader.py
The current example downloads a tiff image, 1500 X 1500 px and 1.5km X 1.5 km.
top_left and bottom_right coordinates and zoom are chosen accordingly.


## splitarea.py
Downloads n images that cover a square area from top_left origin with distance as edge length. It splits the area in images which cover 1.5km X 1.5 km.
The division in tiles of the images sometimes use 7 or 8 tiles per edge. It means that images are not always 1500 px X 1500 px.

## splitimage.py
It dowloads one image that covers a square area from top_left origin with distance as edge length.
It splits the image in tiles 1500 X 1500 px using the imagemagik linux program.
On the borders some tiles can be not 1500 X 1500 px.
