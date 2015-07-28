#!/usr/bin/env python

import os
import time


def main():
	while True:
		for zf in filter(lambda fn:fn.endswith('.zip'), os.listdir(os.getcwd())):
			zfd = zf.replace('.zip','')
			if not os.path.isdir(zfd):
				try:
					open(zf,'r+').close()
					cmd = 'unzip -o "%s"'%zf
					print '%s : %s'%(cmd, os.system(cmd))
				except:
					continue
		time.sleep(5)

if __name__ == '__main__':
	main()

