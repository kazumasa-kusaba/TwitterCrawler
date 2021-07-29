# TwitterCrawler
Crawler to collect user timelines and favorites of any users.  

## Features
* can retrieve user timelines and favorites of any users as JSON files.
* can wait for a reasonable amount of time until the API limits are lifted.

# Installation
Just clone this and start using it.  
```console
git clone git@github.com:kazumasa-kusaba/TwitterCrawler.git
```

## Dependencies
* [requests](https://github.com/psf/requests)  
* [requests-oauthlib](https://github.com/requests/requests-oauthlib)  

Just do:  
```console
pip install requests requests_oauthlib
```

# Usage

## Write your access token infomation
Write your access token information to `config.json` located in the parent directory.    
Replace each preset values with your own informations.  
```json
{
    "twitter_api": {
        "access_token": "ACCESS_TOKEN",
        "access_token_secret": "ACCESS_TOKEN_SECRET",
        "consumer_key": "CONSUMER_KEY",
        "consumer_secret": "CONSUMER_SECRET"
    }
}
```

## Command line options
In general,  
* `-h, --help`: show help
* `-q, --quiet`: do not output log
```console
python twittercrawler.py [-h] [-q] command [target_screen_name [target_screen_name ...]]
```

## Retrieve timelines
If you want to retrieve [@Cristiano (Cristiano Ronaldo)](https://twitter.com/cristiano) and [@BarackObama (Barack Obama)](https://twitter.com/barackobama) timelines...  
```console
python twittercrawler.py retrieve_user_timelines Cristiano BarackObama
```
The retrieved timelines are in the directories (`results/user_timelines/`)

## Retrieve favorites
If you want to retrieve [@Cristiano (Cristiano Ronaldo)](https://twitter.com/cristiano) and [@BarackObama (Barack Obama)](https://twitter.com/barackobama) favorites...  
```console
python twittercrawler.py retrieve_favorites Cristiano BarackObama
```
The retrieved favorites are in the directories (`results/favorites/`)

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

