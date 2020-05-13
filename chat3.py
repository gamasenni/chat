lines = []
with open('lineinput2.txt', 'r', encoding='utf-8-sig') as f :
	for line in f :
		lines.append(line.strip())

for line in lines :
	s = line.split(' ')
	#資料黏一起時，無法用split切割，可以用清單分割法(字串可當清單!)
	time = s[0][:5]
	name = s[0][5:]
	print(time,name)


