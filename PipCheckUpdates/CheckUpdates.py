from win10toast import ToastNotifier
import subprocess
#import os

toast = ToastNotifier()

toast.show_toast("Pip Check Update", "Checking Updates", duration = 10)

#os.chdir("C:\Users\YAG\Downloads\Code\SideQuests\SideQuests")

p = subprocess.Popen(["start", "cmd", "/k", "py -m pip install --upgrade pip setuptools wheel && exit"], shell = True) 



"""
result = subprocess.run(["ls","-l"], capture_output=True , text= True).stdout.decode("utf-8")

result = subprocess.run(["ls","-l"], stdout=subprocess.PIPE).stdout.decode("utf-8")
"""

#s = subprocess.getstatusoutput(p)

#subprocess.check_output(["ls","-l"])

# output = p.communicate()[0]