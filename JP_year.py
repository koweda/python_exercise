year=input('input year:')
jp_y=[1868,1912,1926,1989,2019]
jp_s=["明治","大正","昭和","平成","令和"]

for i in range(5):
    if int(year) >= jp_y[i]:
        output=jp_s[i]+str(int(year)-jp_y[i]+1)

print(output)