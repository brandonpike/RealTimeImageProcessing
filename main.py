import cv2
import imutils as img_util
import numpy as np

flags = {
	"Skeleton":False,
	"None":True
}

def setFlag(flag):
	for k in flags:
		flags[k] = False
	flags[flag] = True
	return

def getModifiedFrame(frame):
	flag = None
	for k in flags:
		if flags[k]:
			flag = k;
	if flag == "None": return frame
	if flag == "Skeleton":
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		return img_util.skeletonize(gray, size=(3, 3))

def main():

	cv2.namedWindow("preview")
	vc = cv2.VideoCapture(0)
	frame = None

	if vc.isOpened(): # try to get the first frame
		rval, frame = vc.read()
	else:
		print("no VC")
		rval = False

	i = 0
	while rval:
		cv2.imshow("preview", frame)
		rval, frame = vc.read()
		frame = getModifiedFrame(frame)
		key = cv2.waitKey(20)
		i += 1
		#print(flags)
		if key == 97: # None
			setFlag("None")
		if key == 98: # Skeleton
			setFlag("Skeleton")
		if key == 27: # exit on ESC
			break

	cv2.destroyWindow("preview")

if __name__ == '__main__':
	main()