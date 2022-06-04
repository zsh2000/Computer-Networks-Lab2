import os
import cv2
import shutil
import time

VIDEO_PATH = 'videos/clip_1.mp4'
EXTRACT_FOLDER = 'test'
EXTRACT_FREQUENCY = 1


def extract_frames(video_path, dst_folder, index):

    video = cv2.VideoCapture(video_path)
    frame_count = 0

    while True:
        _, frame = video.read()
        if frame is None:
            break
        if frame_count % EXTRACT_FREQUENCY == 0:
            save_path = "{}/{:>03d}.jpg".format(dst_folder, index)
            cv2.imwrite(save_path, frame)
            index += 1
        frame_count += 1 

    print(f'the number of frames: {frame_count}')
    print("Totally save {:d} imgs".format(index - 1))

    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

    if int(major_ver) < 3:
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
    else:
        fps = video.get(cv2.CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

    video.release()


def main():
    try:
        shutil.rmtree(EXTRACT_FOLDER)
    except OSError:
        pass
    os.mkdir(EXTRACT_FOLDER)
    extract_frames(VIDEO_PATH, EXTRACT_FOLDER, 1)


if __name__ == '__main__':
    main()
