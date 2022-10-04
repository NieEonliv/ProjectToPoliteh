import cv2
import os
import pathlib
import numpy

def start(input_datadir):
    for dirpath, dirnames, files in os.walk(input_datadir):
        if len(files) == 1:
            if pathlib.Path(dirpath + files[0]).suffix == '.mp4':
                videopath = dirpath + "\\" + files[0]
                print(videopath)
                video_to_frames(videopath)

def video_to_frames(video):
    vidcap = cv2.VideoCapture(video)
    count = 0
    while vidcap.isOpened():
        success, image = vidcap.read() # type: numpy.ndarray
        if success:
            image = numpy.rot90(image)
            image = numpy.rot90(image)
            cv2.imwrite(os.path.join(os.path.dirname(video), '%d.png') % count, image)
            count += 1
        else:
            break
    cv2.destroyAllWindows()
    vidcap.release()
    os.remove(video)
    print('Video read all done, path: ' + video)