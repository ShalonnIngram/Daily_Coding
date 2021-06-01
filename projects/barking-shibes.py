# Use a quotes API, e.g. http://quotes.stormconsultancy.co.uk/random.json
# to fetch a random quote. Then use string manipulation to convert it to
# Doge speech (https://blogs.unimelb.edu.au/sciencecommunication/2016/10/22/how-to-speak-doge/)
# Create a tiny webpage that displays a doge image together
# with the altered quote. You can get an image URL from another API:
# http://shibe.online/api/shibes
# Write the code logic to make the API calls and assign the output to
# `doged_quote` and `doge_image_url` respectively.
# Then write the `html` string to a `.html` file and look at it in your browser.

import random
from pathlib import Path
import requests


image_url = "http://shibe.online/api/shibes"
quote_url = "http://quotes.stormconsultancy.co.uk/random.json"

doged_quote = None
doge_image_url = None

html = (
    f"""<h1>{doged_quote}</h1>
<img src={doge_image_url} width=800>"""
)
