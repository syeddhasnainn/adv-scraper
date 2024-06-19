from fake_headers import Headers

def getHeaders():
    header = Headers(
        browser="chrome",  # Generate only Chrome UA
        os="win",  # Generate ony Windows platform
        headers=True  # generate misc headers
    )

    while True:
        yield header.generate()

headers = getHeaders()
for x in range(5):
    print(next(headers))