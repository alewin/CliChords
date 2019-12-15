## ⚠️ CliChords End of life

```
From <m.chistyakov@ultimate-guitar.com>
Date: 2019-01-28, 07:07 EST

Hi,

I'm Max Chistyakov, Ultimate Guitar developer. Our company found your 
scapper: https://github.com/masterT/ultimate-guitar-scraper

I need to tell you how ultimate-guitar works. First of all, all tabs on 
ultimate-guitar are legal. We pay roaylties to music publishers (Alfred, 
Sony, EMI, etc.) for each tab. If user see ads, we got money from ads 
and transfer money to publicher. If user buy subscription, we send money 
from subscription to publishers. So, ultimate-guitar is just platform 
between music publishers and guitarists. You can read more how licensing 
works here: https://www.ultimate-guitar.com/article/blog/licensing

You created scapper to parse ultimate-guitar.com, nice job. I especially 
admire how quickly you react to changes in our API (Continuous 
Integration is always good idea). But your scapper is illegal. Creating 
software to free show guitar tabalatures/sheetmusic and free 
distribution it is illegal. You can read how few popular websites was 
closed due DMCA 
(https://en.wikipedia.org/wiki/Digital_Millennium_Copyright_Act): 
https://en.wikipedia.org/wiki/On-line_Guitar_Archive, 
https://en.wikipedia.org/wiki/Mxtabs

So, I decide to reach you before lawyers and publishers start working 
and physically found you. I recommend you to delete public repo and npm 
package. May be formatting your disk will be nice for you too.

As developer I'm sorry it happened. But the music industry works that way.


Max
```

---

# CliChords

CliChords is a command line tool that allows you to search and view guitar tabs.

### Install

CliChords requires [Node.js](https://nodejs.org/) to start.

```sh
$ git clone https://github.com/alewin/CliChords
$ cd CliChords
$ npm install / yarn install
$ node clichords
```



### Usage

[![asciicast](https://asciinema.org/a/Gg7Qv6mUAXQlA4GLxZjZWDA4F.png)](https://asciinema.org/a/Gg7Qv6mUAXQlA4GLxZjZWDA4F)


Start CliChords:
```sh
$ node clichords
```
Search tab:
```sh
$ Enter the name of the artist or title of the tab: ******
```
Select ID of the tab :
```sh
$ ID: **
```

### Todos

 - View Ascii chords
 - Add pagination
 - Save and download tabs

License
----

MIT


**Want to contribute? Great!**
