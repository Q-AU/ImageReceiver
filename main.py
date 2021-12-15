import cv2
import numpy as np



def dodge_img(x,y):
    return cv2.divide(x,255-y,scale=256)

def main():
    count=0
    try:
       
                
        print("running script...")
        cam = cv2.VideoCapture(1)
        cv2.namedWindow("test")

        img_counter = 0

        while True:
            ret, frame = cam.read()
            if not ret:
                print("failed to grab frame")
                break
            gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            img_invert=cv2.bitwise_not(gray)
            gblur_img=cv2.GaussianBlur(img_invert,(29,29),sigmaX=0,sigmaY=0)
            dodged_img=dodge_img(gray,gblur_img)
            

            cv2.imshow("test", dodged_img)

            k = cv2.waitKey(1)
            if k%256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k%256 == 32:
                # SPACE pressed
                img_name = "opencv_frame_{}.png".format(img_counter)
                dodge_name = "dodged_frame_{}.png".format(img_counter)

                cv2.imwrite(img_name, frame )        
                cv2.imwrite(dodge_name, dodged_img)        

                print("{} written!".format(img_name))
                img_counter += 1
                count+=1

        cam.release()
        cv2.destroyAllWindows()

        ##To avoit exiting 
       
    except KeyboardInterrupt:
        print("\ninterrupted by user")
        
        

if __name__=='__main__':
    main()        