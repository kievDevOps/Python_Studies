# slicing = create a substring by extracting elements from another string
# indexing[] or slice()
# [start:stop:step]

name = "Kiev DevOps"
first_name = name[0:4] # 0 = K, 1 = i, 2 = e, 3 = v, 4 is excluded
last_name = name[5:11] # 5 = D, 6 = e, 7 = v, 8 = O, 9 = p, 10 = s, 11 = is excluded
step_name = name[0:11:2] # 0 = beginning, 11 = end, 2 = will count 2 by 2
print(first_name)
print(last_name)
print(step_name)

website_1 = "http://google.com"
website_2 = "http://wikipedia.com"
slice = slice(7,-4)
print(website_1[slice])
print(website_2[slice])
# slices are reusable
