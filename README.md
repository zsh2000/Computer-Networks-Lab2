# Computer-Networks-Lab2
Computer Networks Lab2 - 内容的生成与传播

read_video.py读入处理前的视频，拆分出各帧

使用cal_displace.py计算相邻帧之间的L1距离，以探测相机机位切换的时间点

然后通过OpenPose得到对各帧做pose estimation的json file

将相机机位切换的时间点填入代码crop.py L14的list后，对各视频片段进行crop (由于在该case下分割出9段clip，代码L15-16数组的第一个维度从0遍历到8)

最后用make_video.py合成剪辑后的视频
