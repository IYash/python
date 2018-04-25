
# -*- coding: utf-8 -*-
'''
create on 2018-04-25
@Author:hcl
'''
# 获取链接
def get_next_target(page):
    start_link =  page.find('<a href=')
    if start_link == -1:
        return None,0
    start_quote = page.find('"',start_link)
    end_quote = page.find('"',start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url,end_quote


# 收集链接
def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break

if __name__ == '__main__':
    print 'hello world'
