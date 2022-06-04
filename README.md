# Computer-Networks-Lab2
Computer Networks Lab2 - 内容的生成与传播

original_video.mp4是处理前的视频

read_video.py读入处理前的视频，拆分出各帧

然后通过OpenPose得到对各帧做pose estimation的json file

得到机位切换的时间点后，用cal_displace.py对各视频片段进行crop (代码L15-16数组的第一个维度从0遍历到8)

最后用make_video.py合成剪辑后的视频
