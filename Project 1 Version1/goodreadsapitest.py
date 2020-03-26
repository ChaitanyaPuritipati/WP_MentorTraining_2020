import requests
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "iGZG0s5CY0rwO3Muq7Nw0g", "reviews_count": 1})
print(res.json())