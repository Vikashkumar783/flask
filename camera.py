import cv2
import threading
import datetime

class RecordingThread (threading.Thread):
    def __init__(self, name, camera):

        import datetime

        current_time = datetime.datetime.now()

        time="{}{}{}".format(current_time.hour, current_time.minute, current_time.second)
        print(time)

        threading.Thread.__init__(self)
        self.name = name
        self.isRunning = True

        self.cap = camera
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        filename = f'./static/{time}video.avi'
        print(filename)
        self.out = cv2.VideoWriter(filename,fourcc, 20.0, (640,480))
        self.out = cv2.VideoWriter('./static/video.avi',fourcc,20.0,(640,480))
        

    def run(self):
        while self.isRunning:
            ret, frame = self.cap.read()
            if ret:
                self.out.write(frame)

        self.out.release()

    def stop(self):
        self.isRunning = False

    def __del__(self):
        self.out.release()

class Clickimg (threading.Thread):
    def __init__(self,name,camera):
        threading.Thread.__init__(self)
        self.name = name

        self.cap = camera
        import datetime

        current_time = datetime.datetime.now()

        self.time="{}{}{}".format(current_time.hour, current_time.minute, current_time.second)
        
        # check, frame = self.cap.read()
    def run(self):
            print("run click thread")
            check, frame = self.cap.read()
            filename = f'./static/{self.time}image.jpg'
            print(filename,"jjjfjfjfjjfjfjfjjfjfjfjfjfjfjfjfjjfjfjjfjfjjjfjfjjfjfjfjjfjjjgjfjfjjfjfjfjfjjfjfjfjjjj")
            
            cv2.imwrite(filename, img=frame)
            cv2.imwrite('./static/saved_img.jpg',img=frame)
            # self.cap.release()
            print("Processing image...")
            # img_ = cv2.imread('./static/saved_img.jpg', cv2.IMREAD_ANYCOLOR)
            # print("Converting RGB image to grayscale...")
            # gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
            # print("Converted RGB image to grayscale...")
            # print("Resizing image to 28x28 scale...")
            # img_ = cv2.resize(gray,(28,28))
            # print("Resized...")
            # img_resized = cv2.imwrite(filename='./static/saved_img-final.jpg', img=img_)
            print("Image saved!")
            # cv2.imshow("Capturing", frame)

class VideoCamera(object):
    def __init__(self):
        # Open a camera
        self.cap = cv2.VideoCapture(0)
      
        # Initialize video recording environment
        self.is_record = False
        self.out = None

        # Thread for recording
        self.recordingThread = None
        # self.clickimg = None
    
    def __del__(self):
        self.cap.release()
    
    def get_frame(self):
        ret, frame = self.cap.read()

        if ret:
            ret, jpeg = cv2.imencode('.jpg', frame)

            # Record video
            # if self.is_record:
            #     if self.out == None:
            #         fourcc = cv2.VideoWriter_fourcc(*'MJPG')
            #         self.out = cv2.VideoWriter('./static/video.avi',fourcc, 20.0, (640,480))
                
            #     ret, frame = self.cap.read()
            #     if ret:
            #         self.out.write(frame)
            # else:
            #     if self.out != None:
            #         self.out.release()
            #         self.out = None  

            return jpeg.tobytes()
      
        else:
            return None

    def start_record(self):
        self.is_record = True
        print("recording_start")
        self.recordingThread = RecordingThread("Video Recording Thread", self.cap)
        self.recordingThread.start()

    def stop_record(self):
        self.is_record = False
        print("recording stop")

        if self.recordingThread != None:
            self.recordingThread.stop()

    def clickimgage (self):
        
        print("click me ")
        self.clickimg = Clickimg("click img",self.cap)
        self.clickimg.start()

        # self.clickimg.stop()
        # if self.clickimg != None:

    def preview (self):
        print("preview")


            