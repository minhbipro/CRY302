text="""Mucexnyuseic, nu mucexnanyc, ld xiw eusmxlmw spt dxjtc nb xwmiplkjwd bnu dwmjuw mnffjplmsxlnp
lp xiw euwdwpmw nb xilut esuxlwd msaawt sthwudsulwd. Fnuw ywpwusaac, mucexnyuseic ld svnjx
mnpdxujmxlpy spt spsaczlpy eunxnmnad xisx euwhwpx xilut esuxlwd nu xiw ejvalm bunf uwstlpy
eulhsxw fwddsywd; hsulnjd sdewmxd lp lpbnufsxlnp dwmjulxc djmi sd tsxs mnpbltwpxlsalxc, tsxs
lpxwyulxc, sjxiwpxlmsxlnp, spt pnp-uwejtlsxlnp suw mwpxusa xn fntwup mucexnyuseic. Fntwup
mucexnyuseic wrldxd sx xiw lpxwudwmxlnp nb xiw tldmlealpwd nb fsxiwfsxlmd, mnfejxwu dmlwpmw,
wawmxulmsa wpylpwwulpy, mnffjplmsxlnp dmlwpmw, spt eicdlmd. Seealmsxlnpd nb mucexnyuseic
lpmajtw wawmxunplm mnffwumw, mile-vsdwt escfwpx msutd, tlylxsa mjuuwpmlwd, mnfejxwu
esddgnutd, spt flalxsuc mnffjplmsxlnpd"""

f = open("C:\\Users\\minhb\\OneDrive\\Desktop\\corncob_lowercase.txt","r")
word = f.read().split()
word2 = text.replace(",","").replace(";","").replace(".","").lower().split()
tmp = text.replace(",","").replace(";","").replace(".","").lower()

dic = dict()
for i in word2:# tim tat ca cac tu dai hon 10 ky tu
	if len(i)>10:
		dic[i] = i

# print(dic)
key = dict()
for i in dic.keys():# tim tat ca cac tu co the xu dung bang tu dien tieng anh
	index=[]
	possiValue=[pos for pos in word if len(pos)==len(i)]
	for a in i:
		index = [pos for pos, char in enumerate(i) if char == a]
		if len(index) == 2:
			possiValue = [pos for pos in possiValue if pos[index[0]]==pos[index[1]]]
		elif len(index) > 2:
			possiValue = [pos for pos in possiValue if pos[index[0]]==pos[index[1]]==pos[index[2]]]
	# print(i,"co the la:", possiValue)
	if len(possiValue)==1: # thay the toan bo tu co kha nang vao cipher text
		for c in range(len(i)):
			tmp = tmp.replace(i[c],possiValue[0][c].upper())
			# key[i[c]] = possiValue[0][c] # tao key giai ma
# print(tmp)

word2 = tmp.split()
for i in word2:
	if not i.isupper():
		for b in word:
			if len(b)==len(i):
				# print(b)
				match=True
				lower=""
				for char in range(len(i)):
					if i[char].isupper():
						if b[char]!=i[char].lower():
							match=False
							break
					else:
						lower=char
						continue
				if match:
					tmp = tmp.replace(i[lower],b[lower].upper())

# print(tmp.isupper())
print(tmp)
