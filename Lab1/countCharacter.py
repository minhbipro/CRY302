text="""Mucexnyuseic, nu mucexnanyc, ld xiw eusmxlmw spt dxjtc nb xwmiplkjwd bnu dwmjuw mnffjplmsxlnp
lp xiw euwdwpmw nb xilut esuxlwd msaawt sthwudsulwd. Fnuw ywpwusaac, mucexnyuseic ld svnjx
mnpdxujmxlpy spt spsaczlpy eunxnmnad xisx euwhwpx xilut esuxlwd nu xiw ejvalm bunf uwstlpy
eulhsxw fwddsywd; hsulnjd sdewmxd lp lpbnufsxlnp dwmjulxc djmi sd tsxs mnpbltwpxlsalxc, tsxs
lpxwyulxc, sjxiwpxlmsxlnp, spt pnp-uwejtlsxlnp suw mwpxusa xn fntwup mucexnyuseic. Fntwup
mucexnyuseic wrldxd sx xiw lpxwudwmxlnp nb xiw tldmlealpwd nb fsxiwfsxlmd, mnfejxwu dmlwpmw,
wawmxulmsa wpylpwwulpy, mnffjplmsxlnp dmlwpmw, spt eicdlmd. Seealmsxlnpd nb mucexnyuseic
lpmajtw wawmxunplm mnffwumw, mile-vsdwt escfwpx msutd, tlylxsa mjuuwpmlwd, mnfejxwu
esddgnutd, spt flalxsuc mnffjplmsxlnpd"""

tmp=text.lower()
feq= dict()
total=0
for i in tmp:
	if i.isalpha():
		total+=1
		feq[i]=feq.get(i,0)+1
feq = dict(sorted(feq.items(), key=lambda item: item[1], reverse=True))
for u,v in feq.items():
	print(u,"{:.2f}%".format(v/total*100))
