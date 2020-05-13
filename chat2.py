def read_file(filename) :
	lines = []
	with open (filename, 'r', encoding='utf-8') as f :
		for line in f :
			lines.append(line.strip())
	return lines


def convert(lines):
	person = None
	Hsin_word_count = 0
	duck_word_count = 0
	Hsin_sticker_count = 0
	duck_sticker_count = 0
	Hsin_image_count = 0
	duck_image_count = 0
	for line in lines :
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Hsin' :
			if s[2] == '貼圖' :
				Hsin_sticker_count += 1
			elif s[2] == '圖片' :
				Hsin_image_count += 1
			else:
				for m in s[2:] :
					Hsin_word_count += len(m)

		elif name == '小鴨' :
			if s[2] == '貼圖' :
				duck_sticker_count += 1
			elif s[2] == '圖片' :
				duck_image_count += 1
			else :	
				for m in s[2:] :
					duck_word_count += len(m)

	print('Hsin說了', Hsin_word_count, '個字，傳了', Hsin_sticker_count, '個貼圖,傳了', Hsin_image_count, '個圖片!')
	print('小鴨說了', duck_word_count, '個字，傳了', duck_sticker_count, '個貼圖,傳了', duck_image_count, '個圖片!')


def write_file(filename,lines):
	with open(filename, 'w', encoding='utf-8') as f :
		for line in lines :
			f.write(line + '\n')


def main() :
	lines = read_file('lineinput.txt')
	lines = convert(lines)
	#write_file('lineoutput.txt', lines)

main()