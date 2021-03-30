import cv2

def test():
    img = cv2.imread('photo_video/lena.jpg')
    while True:
        cv2.imshow('photo_video/lena image', img)
        
        # 若按下 q 鍵則離開迴圈
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print('I am done')
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    test()