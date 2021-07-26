# TwitterCrawler
Crawler to collect tweets and favorites of any user

# Installation
Just clone this and start using it.  
```console
git clone git@github.com:kazumasa-kusaba/TwitterCrawler.git
```

## Dependencies
**TODO: write here**
* [temp](http://temp.com)  
* [temp](http://temp.com)  
Just do:  
```console
pip install XXX
pip install XXX
pip install XXX
```

# Usage

## Write the access token infomation

**TODO: write here**

## Command line options
In general,  
* `--command`: the command you want to run
* `--target-screen-name`: screen name of the target name
* `--quite`: do not output log
* `--help`: show help

## Get tweets
* `--command`: `get_tweets`
* `--target-screen-name`: any screen names you want to get tweets from

ex) If you want to get [@Cristiano (Cristiano Ronaldo)](https://twitter.com/cristiano) and [@BarackObama (Barack Obama)](https://twitter.com/barackobama) tweets...  
```console
python twittercrawler.py --command get_tweets --target-screen-name Cristiano BarackObama
```

## Get favorites
* `--command`: `get_favorites`
* `--target-screen-name`: any screen names you want to get favorites from

ex) If you want to get [@Cristiano (Cristiano Ronaldo)](https://twitter.com/cristiano) and [@BarackObama (Barack Obama)](https://twitter.com/barackobama) favorites...  
```console
python twittercrawler.py --command get_favorites --target-screen-name Cristiano BarackObama
```

# License
```
MIT License

Copyright (c) 2021 Kazumasa Kusaba

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

