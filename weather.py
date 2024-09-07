from requests_html import HTMLSession
#import Speech_to_text


def weather(q):
    s = HTMLSession()
    url = f'https://www.google.com/search?q=weather+{q}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}
    r = s.get(url, headers=headers)
    temp = r.html.find('div.vk_bk.TylWce.SGNhVe span.wob_t.q8U8x', first=True).text
    unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first = True).texts
    desc = r.html.find('span#wob_dc', first = True).text
    return temp + " " + unit + " " + desc

a = input("Enter Location: ")
print(weather(a))