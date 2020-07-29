import numpy as np
import cv2
import os
import sys
import matplotlib.image as mpimg

folder2 = sys.argv[1]
folder1 = sys.argv[2]

img1 = []
img2 = []
a = str("20171054_")
a = a+"20171179_"
a = a+"2018121005"
a = a+".txt"
f = open(a,"a")

for file1 in os.listdir(folder1):
	cur = folder1+file1
	img = mpimg.imread(cur)
	img = cv2.resize(img,(1080,1080))
	# print(img)
	flat_img = img.flatten()
	b = [flat_img,file1]
	img1.append(b)

for file2 in os.listdir(folder2):
	cur = folder2+file2
	img = mpimg.imread(cur)
	img = cv2.resize(img,(1080,1080))
	flat_img = img.flatten()
	a = [flat_img,file2]
	img2.append(a)
correct = 0
wrong = 0
ans = 0

for i,ind1 in img1:
	max1 = -1
	# print(i)
	for j,ind2 in img2:
		# a = signal.correlate2d(i,j)
		product = np.mean((i - i.mean()) * (j - j.mean()))
		stds = i.std() * j.std()
		if stds == 0:
			ans = 0
		else:
			ans = product/stds
		# print(ans)
		if ans>max1:
			store = ind2
			max1 = ans
	f.write("%s %s" % (ind1, store))
	f.write("\n")
	if ind1.split('#')[0] == store.split('#')[0]:
		correct+=1
	else:
		wrong+=1
final = correct/(correct+wrong)
final = final*100
f.close()


