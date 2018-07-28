# Generating my first valid Content-Security-Policy

I have a tiny webapp to which I'd like to introduce Content-Security-Policy. 

However I'm having trouble generating a valid header.

  - `index.html` is a tiny HTML file
  - `script.js` console.logs 'hallo'
  - `serve.py` is a tiny webserver that injects the CSP header, run it with `python serve.py`

If I'm understanding right, so long as I present the sha256 of script.js in the header, things should work.

## I'm using report-uri.com's [hashing utility](https://report-uri.com/home/hash)
  Paste in contents of script.js

  Get this value back:
  sha256-uybHLI+qDunPRU2zC6ky8w1ywagNzyQn4XzCpBw8pp4=

  Paste it into serve.py:11

  No bueno?