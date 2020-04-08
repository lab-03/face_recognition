import urllib.request
# Download the file from `url`, save it in a temporary directory and get the
# path to it (e.g. '/tmp/tmpb48zma.txt') in the `file_name` variable:
def url_to_image(url):
    file_name = urllib.request.urlretrieve(url)[0]
    return file_name