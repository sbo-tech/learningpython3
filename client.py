import urllib.request
# contents = urllib.request.urlopen("http://example.com/foo/bar").read()

def fetch():
    response_type = "code"
    client_id = "Jzqt67xbNKfViwr6y87UOgBq5JYar68Ix3HK7PRK"
    redirect_uri = "http://localhost:81"
    scope = "read,write,introspection"


    contents = urllib.request.urlopen("https://admin.sbo.tech/oauth2/authorize/?response_type=" + response_type + "&client_id=" + client_id + "&redirect_uri=" + redirect_uri  + "&scope=" + scope)
    x = contents.geturl() #.read()
    print(x)
    return contents

if __name__ == '__main__':
    fetch()