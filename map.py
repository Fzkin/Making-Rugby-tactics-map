import numpy as np  
import cv2
#import math

def saveImg(A,name):
    cv2.imwrite('%s.jpg'%(name),A,[int(cv2.IMWRITE_JPEG_QUALITY),70])

    print('保存成功')
def initImg(x,y,lt_l=0,lt_r=0,lg_l=0,lg_r=0,c_l=0,c_r=0,rg_l=0,rg_r=0,rt_l=0,rt_r=0):
    img = np.zeros((x,y,3), np.uint8)   
    #fill the image with white
    img.fill(255)
    #上宽50 左宽35  左上角35 50 
    img = line(img,35,25,35,275)
    img = line(img,565,25,565,275)
    for k in range(6):
        print(k)
        
        img = line(img,35,25+50*k,565,25+50*k) 
#        if k == 0:
#            pass
#        elif k==5:
#            pass
#        else:
#            img = conment(img,570,25+50*k,'%s'%(str(50 - k*5)))
    img = circle(img,260,229,lt_l,lt_r)
    img = circle(img,280,229,lg_l,lg_r)
    img = square(img,300,225,c_l,c_r)
    img = circle(img,320,229,rg_l,rg_r)
    img = circle(img,340,229,rt_l,rt_r)
    img = circle(img,200,199)
    img = circle(img,230,189)
    img = circle(img,250,189)
    img = circle(img,280,179)
    img = circle(img,320,179)
    img = circle(img,350,189)
    img = circle(img,370,189)
    img = circle(img,400,199)
    
    img = circle(img,100,233)
    img = circle(img,180,230)
    img = circle(img,420,230)
    img = circle(img,500,233)
    
    
    img = circle(img,100,199)
    img = circle(img,500,199)
    img = circle(img,300,129)
    print('初始化成功')
    return img
def circle(img,x,y,l=0,r=0):
    if l == 1:
        img = line(img,x-8,y-12,x-2,y-12)
    if r == 1:
        img = line(img,x+8,y-12,x+2,y-12)
    img = cv2.circle(img,(x,y), 8, (0,0,1), 1)
    return img
def square(img,x,y,c_l,c_r):
    img = cv2.rectangle(img,(x-8,y-8),(x+8,y+8),(0,0,1),1)
    if c_l == 1:
        img = line(img,x-10,y,x-2,y-12)
    if c_r == 1:
        img = line(img,x+10,y,x+2,y-12)
    return img
def line(img,x1,y1,x2,y2,isnoArrow=-1,lineType  = cv2.LINE_AA): 
    thickness = 1 
    img = cv2.line(img, (x1,y1), (x2,y2), (0,0,1), thickness, lineType)
    if isnoArrow == -1:
        pass
    else:
        type = isnoArrow
        img = Arrow(img,x2,y2,type)
    print('画直线成功',x1,y1,x2,y2)
    return img

def Arrow(img,x,y,type):
    if type == 0:
        img = line(img,x,y,x - 5,y + 5)
        img = line(img,x,y,x + 5,y + 5)
        return img
    elif type == 1:
        img = line(img,x,y,x - 5,y - 5)
        img = line(img,x,y,x + 5,y - 5)
    
    elif type == 2:
        img = line(img,x,y,x + 5,y - 5)
        img = line(img,x,y,x + 5,y + 5)
    elif type == 3:
        img = line(img,x,y,x - 5,y - 5)
        img = line(img,x,y,x - 5,y + 5)
    elif type == 4:
        img = line(img,x,y,x - 5,y)
        img = line(img,x,y,x,y + 5)
    elif type == 5:
        img = line(img,x,y,x + 5,y)
        img = line(img,x,y,x,y + 5)
    elif type == 6:
        img = line(img,x,y,x + 5,y)
        img = line(img,x,y,x,y - 5)
    elif type == 7:
        img = line(img,x,y,x - 5,y)
        img = line(img,x,y,x,y - 5)

    
    return img
def conment(img,x,y,text):
    font=cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img,'%s'%(text),(x,y), font, 0.4,(0,0,1),1)
    return img
    

def RotateClockWise90(img):
    trans_img = cv2.transpose( img )
    img = cv2.flip(trans_img, 1)
    trans_img = cv2.transpose( img )
    new_img = cv2.flip(trans_img, 1)
    return new_img



#img = initImg(300,600)
#line(img,35,50,565,50,0)

#saveImg(img,'cover2')
centerLine_l_x = 280-50
centerLine_l_y = 179-30
centerLine_r_x = 320+50
centerLine_r_y = 179-30

name = ['cover3_normal_23qk','cover3_normal_23qA','cover3_normal_23jk','cover3_normal_23jA','cover3_normal_24qk','cover3_normal_24qA','cover3_normal_24jk','cover3_normal_24jA','cover3_31_234Q_rush','cover3_13_2QKA_rush','cover3_solo4_rush','cover3_c_l_rush','cover3_c_r_rush','cover3_safty_rush','cover3_33_234QKA_rush']
for i in name:
    if i == 'cover3_normal_23qk':
        #机密  手动滑稽

        saveImg(img,i)
    elif i == 'cover3_normal_23qA':
        
        saveImg(img,i)
    elif i == 'cover3_normal_23jk':
        
        saveImg(img,i)
    elif i == 'cover3_normal_23jA':
        
        saveImg(img,i)
    elif i == 'cover3_normal_24qk':
        saveImg(img,i)
    elif i == 'cover3_normal_24qA':
        saveImg(img,i)
    elif i == 'cover3_normal_24jk':
        saveImg(img,i)
    elif i == 'cover3_normal_24jA':
        saveImg(img,i)
    
    elif i == 'cover3_31_234Q_rush':
        saveImg(img,i)

    elif i == 'cover3_13_2QKA_rush':
        saveImg(img,i)
    elif i == 'cover3_solo4_rush':
        saveImg(img,i)
    elif i == 'cover3_safty_rush':
        saveImg(img,i)
        
    elif i == 'cover3_33_234QKA_rush':
        saveImg(img,i)
    elif i == 'cover3_c_l_rush':
        saveImg(img,i)
    elif i == 'cover3_c_r_rush':
        saveImg(img,i)
    else:
        pass


#左上角 71 145  右上角  916 144
#71 229
#71 324
#71 
# 530   250      600*300     





    

