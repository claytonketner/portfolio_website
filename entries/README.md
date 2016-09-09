I made my own special markdown/shorthand for html that gets expanded by the
`python manage.py load_entries` command.

Images
===========

Image size
-------------
`<img>` tags get wrapped in a div with bootstrap `col-*` classes that will
make multiple images show up in a 2-column format. If you're doing this, wrap
all adjacent images in a div like this:
```
<div class="multi-img row">
    <img src="image1.jpg"/>
    <img src="image2.jpg"/>
    <img src="image3.jpg"/>
</div>
```

OR

If you want your image to be full width, put `big` inside the img tag, like
```
<img big src="/path/to/image.jpg"/>
```


Image captions
-----------------
If you want your image to have a caption, give it the `caption` attribute:
```
<img src="/path/to/image.jpg" caption="My image caption."/>
```
