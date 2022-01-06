# Welcome to WikiFlix!

## What is Wikiflix? 
WikiFlix animates all of the revisions to a given Wikipedia page. 
It does it by scraping image data from a headless Chromium browser, 
and displaying it in a Matplotlib applet. 
Scraping and display happens in a live event loop, 
so there is no need to store any image data to disk in order to run the animation.

## How to use it

```python
>>> import wikiflix
>>>
>>> wikiflix.play('Compost')
```


