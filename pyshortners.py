import pyshorteners
link = input("enter here")
short = pyshorteners.Shortener()
x = short.tinyurl.short(link)
print(x)

