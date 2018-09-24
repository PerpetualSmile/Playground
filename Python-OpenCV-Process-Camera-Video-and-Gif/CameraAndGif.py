# 打开摄像头拍摄并制作延时摄影和GIF
import cv2
import time
import os
import shutil
from PIL import Image

interval = 1  # 捕获图像的间隔，单位：秒
num_frames = 100   # 捕获图像的总帧数
out_fps = 24    # 输出文件的帧率

# VideoCapture(0)表示打开默认的相机
cap = cv2.VideoCapture(0)

# 获取捕获的分辨率
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# 设置要保存视频的编码，分辨率和帧率
video = cv2.VideoWriter(
    "time_lapse.avi",
    cv2.VideoWriter_fourcc('M', 'P', '4', '2'),
    out_fps,
    size
)

# 对于一些低画质的摄像头，前面的帧可能不稳定， 略过
for i in range(42):
    _, n = cap.read()

if not os.path.exists("frames"):
    os.makedirs('frames')
try:
    for i in range(num_frames):
        _, frame = cap.read()
        video.write(frame)
        # 如果希望每一帧也存成文件，比如制作GIF，则取消下面的注释
        filename = '{}.png'.format(i)
        cv2.imwrite('frames/' + filename, frame)
        print('Frame {} is captured.'.format(i))
        time.sleep(interval)
except KeyboardInterrupt:
    # 提前停止捕获
    print('Stopped! {}/{} frames captured.'.format(i, num_frames))

# 释放资源并写入视频文件
video.release()
cap.release()

# 将保存的图片制作成gif
im = Image.open("frames\\0.png")
images = []
size = (int(im.size[0]/2), int(im.size[1]/2))
for file in range(1, num_frames):
    filepath = "frames\\" + str(file) + ".png"
    temp = Image.open(filepath)
    temp = temp.resize(size, Image.ANTIALIAS)
    images.append(temp)

im = im.resize(size, Image.ANTIALIAS)
im.save('save.gif', save_all=True, append_images=images, loop=2, duration=5)

# 删除保存中间图片文件的文件夹
shutil.rmtree("frames")