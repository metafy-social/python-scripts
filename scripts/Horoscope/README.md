# Horoscope

> Python script to read day to day horoscope.

## Introduction

Horoscope Reader takes zodiac sign and gives out the horoscope readings for the given day. Information is obtained from [horoscope.com](https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=1) using web scraping technique.

## Dependencies

Horoscope Reader uses `beautifulsoup` to scrape information from web and `requests` to fetch the webpage of [horoscope.com](https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=1).

### Install the dependencies

To install dependencies run the command : 

```bash
$ pip install -r requirements.txt 
```

This will install `beautifulsoup` and `requests` (if you dont have already).


## Usage

Run the script.py

### Input

Input the number that corresponds to the zodiac sign. eg: If the sign is Cancer then input `4`.

```
Enter your Zodiac sign:
[1] Aries
[2] Taurus
[3] Gemini
[4] Cancer
[5] Leo
[6] Virgo
[7] Libra
[8] Scorpio
[9] Sagittarius
[10] Capricorn
[11] Aquarius
[12] Pisces
> 4
```

Input the number corresponding to the day you want to check. eg: If you want to check for yesterday then input `1`

```
Choose Day:
[1] Yesterday   [2] Today       [3] Tomorrow:
> 1
```

### Output

Outputs the horoscope reading. If you want to continue press `y` or press `n` to quit.

```
Horoscope Reading
---------------------------------------------

Oct 9, 2022 - Compliments are apt to feel like gold to you, Taurus. There's nothing you need more than love and affection on a day like this. Beware that you may end up as putty in the hands of whoever showers you with flattery. You may also resent this need for attention and not be willing to receive it graciously. This isn't the right attitude. Receive accolades with open arms and offer an equal amount of affection in return.

Do you want to read horoscope again [y/n] >
```

## Author : Samartha | [@yunghog](https://github.com/yunghog)
