import cv2
import numpy as np
import json
def my2str(i):
	if i<10:
		return "00"+str(i)
	elif i<100:
		return "0"+str(i)
	else:
		return str(i)


def cal(central_point):
    t1 = central_point[1]-450
    t2 = central_point[1]+450
    t3 = central_point[0]-250
    t4 = central_point[0]+250
    if central_point[1] - 450 < 0:
        t1 = 0
        t2 = 900
    if central_point[1] + 450 > 1080:
        t1 = 1080 - 900
        t2 = 1080
    if central_point[0] - 250 < 0:
        t3 = 0
        t4 = 500
    if central_point[0] + 250 > 1920:
        t3 = 1920 - 500
        t4 = 1920
    return np.array([t1, t2, t3, t4])
    

start_end_list = [(1,31), (36,71), (76,146), (151, 186), (191, 256), (261, 321), (326, 336), (341, 386), (391, 411)]  # fill in the list according to the time stamps found by calculating L1 distance between adjacent frames
list_len = len(start_end_list)
    
anchor_interval = 5

for list_id in range(list_len):
    start_frame = int(start_end_list[0][0])
    end_frame = int(start_end_list[0][1])

    anchor_frame = {}

    for i in range(start_frame, end_frame + 1, anchor_interval):
        json_file = "./output_jsons/"+my2str(i)+"_keypoints.json"
        with open(json_file) as jf:
            content = json.load(jf)
        
            central_point = []
            x_y_range = []
        
            for person_num in range(len(content["people"])):
                print(i)
                pose_2d = np.array(content["people"][person_num]["pose_keypoints_2d"]).reshape(25, 3)
            
                valid_joint = 0
                sum_x = 0
                sum_y = 0
            
                max_x = -1
                max_y = -1
                min_x = 10000
                min_y = 10000
             
                for joint_num in range(25):
                    if pose_2d[joint_num][2] != 0:
                        valid_joint += 1
                        sum_x += pose_2d[joint_num][0]
                        sum_y += pose_2d[joint_num][1]
                       
                        if pose_2d[joint_num][0] < min_x:
                            min_x = pose_2d[joint_num][0]
                        elif pose_2d[joint_num][1] < min_y:
                            min_y = pose_2d[joint_num][1]
                    
                        if pose_2d[joint_num][0] > max_x:
                            max_x = pose_2d[joint_num][0]
                        elif pose_2d[joint_num][1] > max_y:
                            max_y = pose_2d[joint_num][1]
            
            
                if valid_joint >= 5:
                    average_x = sum_x/valid_joint
                    average_y = sum_y/valid_joint
                    central_point.append((average_x, average_y))
                    x_y_range.append((min_x, max_x, min_y, max_y))
             
            right_most = -1
            right_most_idx = 0        
            for iter_num in range(len(central_point)):
                if central_point[iter_num][0] > right_most:
                    right_most = central_point[iter_num][0]
                    right_most_idx = iter_num
            
            crop_center = central_point[right_most_idx]
            crop_range = x_y_range[right_most_idx]
        
            print(crop_center, crop_range)
        
            anchor_frame[i] = crop_center

    for i in range(start_frame, end_frame+1, 5):
        img = cv2.imread("./test/"+my2str(i)+".jpg")
    
        curr_range = cal(anchor_frame[i])
        print(img.shape)
        img = img[int(curr_range[0]): int(curr_range[1]), int(curr_range[2]): int(curr_range[3])]
    
        cv2.imwrite("./cropped/"+my2str(i)+".jpg", img)
    
        if i+5 < end_frame+1:
            img = cv2.imread("./test/"+my2str(i+1)+".jpg")
        
            curr_range = cal(np.array(anchor_frame[i])*0.8 + np.array(anchor_frame[i+5])*0.2)
            img = img[int(curr_range[0]): int(curr_range[1]), int(curr_range[2]): int(curr_range[3])]
            cv2.imwrite("./cropped/"+my2str(i+1)+".jpg", img)
        

            img = cv2.imread("./test/"+my2str(i+2)+".jpg")
        
            curr_range = cal(np.array(anchor_frame[i])*0.6 + np.array(anchor_frame[i+5])*0.4)
            img = img[int(curr_range[0]): int(curr_range[1]), int(curr_range[2]): int(curr_range[3])]
            cv2.imwrite("./cropped/"+my2str(i+2)+".jpg", img)

        
            img = cv2.imread("./test/"+my2str(i+3)+".jpg")
         
            curr_range = cal(np.array(anchor_frame[i])*0.4 + np.array(anchor_frame[i+5])*0.6)
            img = img[int(curr_range[0]): int(curr_range[1]), int(curr_range[2]): int(curr_range[3])]
            cv2.imwrite("./cropped/"+my2str(i+3)+".jpg", img)

        
            img = cv2.imread("./test/"+my2str(i+4)+".jpg")
        
            curr_range = cal(np.array(anchor_frame[i])*0.2 + np.array(anchor_frame[i+5])*0.8)
            img = img[int(curr_range[0]): int(curr_range[1]), int(curr_range[2]): int(curr_range[3])]
            cv2.imwrite("./cropped/"+my2str(i+4)+".jpg", img)