import blockspring
import json

print blockspring.runParsed("parse-rss-feed-to-json", { "feed_url": "http://www.humanitarianresponse.info/api/v1.0/assessments", "num_items": 20 }).params
