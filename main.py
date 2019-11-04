#coding:utf-8
#configuration base renderdata
filename=str(input("请输入文件名:"))

class img_reder:
    rate_default=25
    width_img=1920
    height_img=1080
    date_format='jpeg'

#check userID and applicationID     
try:
	while True:
	    uid=int(input("请输入ID:"))
	    if(uid !=''):
	    	print("ID检验完成")
	    	list1=[uid]
	    break    
	
	print("当前用户ID为:",list1)
except ValueError:
	print("数据类型错误,仅支持数字,不能为空，不能是字符或者符号!")
	

def evn_path():
    os.execute("set %path%='c:\Users\zuojialin\desktop\'")
    
               
