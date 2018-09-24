import cv2
import os
import sys, argparse

def main():
    parser = argparse.ArgumentParser(description="Process videos and capture the frame.")
    parser.add_argument('-path', dest='path', required=False)
    parser.add_argument('-interval', dest='frame_interval', required=False)
    args = parser.parse_args()

    path = '.'
    if args.path:
        path = args.path
    
    frame_interval = 10
    if args.frame_interval:
        frame_interval = args.frame_interval
    
    filenames = os.listdir(path)
    filenames = [file for file in filenames if not file.endswith('.py')]
    frame_path = 'result'
    if not os.path.exists(frame_path):
        os.mkdir(frame_path)
    
    cap = cv2.VideoCapture()
    for filename in filenames:
        filepath = os.sep.join([path, filename])

        # VideoCapture::open函数从文件获取视频
        cap.open(filepath)

        # 获取视频帧数
        n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        # 避免视频开头几帧质量低下，黑屏或者无关等
        for i in range(42):
            cap.read()
        for i in range(n_frames-42):
            ret, frame = cap.read()

            # 每隔frame_interval帧进行一次截屏操作
            if i % frame_interval == 0:
                imagename = '{}_{:0>6d}.jpg'.format(filename.split('.')[0], i)
                imagepath = os.sep.join([frame_path, imagename])
                print('exported {}!'.format(imagepath))
                cv2.imwrite(imagepath, frame)
    cap.release()


if __name__ == '__main__':
    main()


