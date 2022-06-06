# Computer-Networks-Lab2
Computer Networks Lab2 - 内容的生成与传播

read_video.py读入处理前的视频，拆分出各帧

使用cal_displace.py计算相邻帧之间的L1距离，以探测相机机位切换的时间点

然后通过OpenPose得到对各帧做pose estimation的json file

将相机机位切换的时间点填入代码crop.py (L33) 的list后，用crop.py对各视频片段进行裁剪。目标是裁剪出最右边的人物，并resize成500×900的符合抖音竖屏习惯的视频

最后用make_video.py合成剪辑后的视频
