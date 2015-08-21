import sys
import os
import getopt
import Image

def tran(fn, sfn, color_dic):
	img = Image.open(fn)
	w,h = img.size
	for n in xrange(w):
		for m in xrange(h):
			r,g,b,a = img.getpixel((n,m))
			sc = (r,g,b)
			if sc in color_dic:
				t = color_dic[sc]
				img.putpixel((n,m), (t[0],t[1],t[2], a))
	img.save(sfn)

def parsev(s):
	s = s.strip()
	if len(s)==3:
		s = s[0]+s[0]+s[1]+s[1]+s[2]+s[2]
	v = int(s,16)
	v = ((v>>16)&0x00ff, (v>>8)&0x00ff, v&0x00ff)
	return v

def parsel(s):
	ix = s.index(':')
	return (parsev(s[0:ix]), parsev(s[ix+1:]))

def parsed(s):
	d = {}
	for l in s.split(";"):
		k,v = parsel(l)
		d[k] = v
	return d


def main():
	from optparse import OptionParser
	parser = OptionParser()
	parser.add_option("-f", "--src",action = "store", type="string", dest="srcimg")
	parser.add_option("-o", "--dst", type="string", dest="dstimg")
	parser.add_option("-m", "--map", type="string", dest="colormap", default="000000:ffffff")
	opts, args = parser.parse_args(sys.argv[1:])

	if opts.srcimg:
		if not opts.dstimg:
			opts.dstimg = opts.srcimg.replace(".png","_out.png")
		tran(opts.srcimg, opts.dstimg, parsed(opts.colormap))
	else:
		print 'not input file'

if __name__ == '__main__':
	main()
