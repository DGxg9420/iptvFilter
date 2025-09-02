import re
import httpx


def get_js_content():
    """
    异步获取URL内容
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }
    url = "https://ghproxy.link/js/src_views_home_HomeView_vue.js"
    response = httpx.get(url, headers=headers)
    return response.text


def parse_proxy_url(js_text):
    """
    解析代理URL
    """
    result = re.search(r"<a href=\\+\"(.*?)\\+.*?data-v-5848117a>", js_text)
    proxy_url = result.group(1) if result else "https://ghfast.top/"
    print("代理URL:", proxy_url)
    return proxy_url


def replace_proxy_url(proxy_url):
    """
    替换代理URL
    """
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
    result = re.search(r'(http.*?https://raw.githubusercontent.com/DGxg9420/iptvFilter/refs/heads/master/group_channels.m3u8)',  content)
    old_url = result.group(1)
    print("旧URL:", old_url)
    new_proxy_url = proxy_url + "/https://raw.githubusercontent.com/DGxg9420/iptvFilter/refs/heads/master/group_channels.m3u8"
    print("新URL:", new_proxy_url)
    content = content.replace(old_url, new_proxy_url)
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == '__main__':
    js_text = get_js_content()
    proxy_url = parse_proxy_url(js_text)
    replace_proxy_url(proxy_url)