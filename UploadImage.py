import pycurl

url = "http://imhttp.mintcode.com/launchr/api/upload"
curl = pycurl.Curl()
curl.setopt(pycurl.URL, url)
curl.setopt(pycurl.POST, 1)
curl.setopt(pycurl.HTTPHEADER, [
    "Content-Type: application/json",
    "Accept: application/json",
    "User-Agent: Android 6.0",
    "Connection: Keep-Alive",
    "Accept-Encoding: gzip",
    "Accept-Charset: UTF-8"
])
curl.perform()
curl.close()
print curl.getinfo(pycurl.CONTENT_TYPE)
