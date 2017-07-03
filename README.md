# blender_split_bodies

Blender addon to take a packed 3d printer plate STL and separate the bodies and export individual STLs

# Instructions:

## Install:

* Download the python file and save it somewhere
* Open blender's user preferences -> addons -> install addon from file and select the addon
* Enable it

## Use:

* Set your scene output directory (you ___MUST___ do this as this will the the output directory, you will not be asked for an output directory. If you have no directory set, you'll see a big scary python error message.)![](https://github.com/ntoff/blender_split_bodies/blob/master/output.PNG)
* Import your packed plate stl
* Highlight it
* Bring up the search menu and type "split bodies", click on it. Your file will (or _should_ if it worked) be split up into individual pieces and exported as separate STL's.

_There's a good chance your original packed plate will be overwritten if the output directory is the same as the directory where the packed plate stl resides. If you wish to keep it safe, set your output directory to an empty one._

## Notes:

You will never be asked for an output directory, you must set your output directory in blender under the render options menu. You will never be asked if you wish to overwrite the output file so be careful.

Don't post bug reports asking for help on how to use blender, or how to bring up the search menu, or how to install an addon. There are enough tutorials on the internet on how to use blender, I'm not a blend-fu wizard, I know just enough to get by.

## ToDo:

* Possibly some error checking in case there's no output directory set? (probably not)
* A button somewhere or a menu entry instead of / as well as the popup search menu entry (although I much prefer keyboard control)
* Other stuff I haven't thought of yet
