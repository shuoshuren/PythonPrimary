url = "http://www.baidu.com/1.jpg"

# 1.判断是否以指定字符串开始
print(url.startswith("http"))
# 2.判断是否以指定字符串结束
print(url.endswith("jpg"))

# 3.查找指定字符串,如果找不到则返回-1
print(url.find("www"))
# index同样可以查找指定字符串在大字符串中的位置，如果不存在则报错
print(url.find("abc"))

# 4.替换字符串,replace会返回一个新的字符串，不会修改原有的字符串内容
new_url = url.replace("baidu","qq")
print(url)
print(new_url)