# Generating my first valid Content-Security-Policy

I have a tiny webapp to which I'd like to introduce Content-Security-Policy. However I'm having trouble generating a valid one.

  - `index.html` is a tiny HTML file
  - `script.js` console.logs 'hallo'
  - `serve.py` is a tiny webserver that injects the CSP header, run it with `python serve.py`

## report-uri.com provides a hashing utility
  https://report-uri.com/home/hash
  Paste in script.js
  Paste this into my header:
  sha256-uybHLI+qDunPRU2zC6ky8w1ywagNzyQn4XzCpBw8pp4=

  