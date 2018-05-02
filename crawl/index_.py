# -*- coding: utf-8 -*-
# 添加页面索引，索引的数据结构[keyword,[url]]
def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

# 根据索引查找url
def lookup(index,keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return []

# it should update the index to include all of the word
# accurences found in the page content by adding the url to the
# word's associated url list
def add_page_to_index(index,url,content):
   words = content.split()
   for word in words:
       add_to_index(index,word,url)
        
