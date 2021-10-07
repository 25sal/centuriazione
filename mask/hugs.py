import cv2
import numpy as np


def hugs(filename, outfile):
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,10,600,apertureSize = 3)

    lines = cv2.HoughLines(edges,1,np.pi/180,120)
    img.fill(255)
    for line in lines:
        for rho,theta in line:
            if rho > 0:
                print(rho, theta)
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a*rho
                y0 = b*rho
                x1 = int(x0 + 1000*(-b))
                y1 = int(y0 + 1000*(a))
                x2 = int(x0 - 1000*(-b))
                y2 = int(y0 - 1000*(a))

                cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

    cv2.imwrite(outfile,img)


if __name__ == "__main__":
    hugs('images/Capodrise_40.png', 'images/result.png')