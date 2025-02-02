from seleniumbase import SB
import time 
def read(filename):
    with open(filename, "r") as f:
        html = f.read()
    return html

def write(filename, html):
    with open(filename, "w") as f:
        f.write(html)

# with SB(uc=True, test=True, incognito=True) as sb:
#     url = "https://www.zillow.com/apartments/san-diego-ca/montanosa/5XjSQf/"
#     sb.open(url)
#     time.sleep(10)
#     html = sb.get_page_source()
#     print(html[:10])
#     write("home.html", html)
