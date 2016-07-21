import os
import sys
trace="/opt/smalltool/"
hostsfile="/opt/smalltool/hostsfile/"
# def makehostsfile():
# 	if not os.path.exists(trace+"/hostsfile"):
# 		os.system("sudo mkdir "+trace+"/hostsfile");
# 	return;
def judge():
	if  os.path.exists("/etc/hosts"): #and os.path.exists(hostsfile+"lasthosts"):
		print "switch  success";
	else:
		print "switch  fail!!!";
	return;
def isExists(file):
	if os.path.exists(file):
		return True;
	else:
		print file+"  is not exists";
		return False

def help():
	print "-h           help"
	print "ls           ls /opt/smalltool/hostsfile/"
	print "cat          cat /etc/hosts"
	print "vi <file>    create  a file an save in /opt/smalltool/hostsfile/"
	print "<file>       switch hosts "
	pass
#####################
#makehostsfile();
i=0;
for arg in sys.argv:
	 i=i+1;
	 if arg == "ls":
	 	print "you has these hostsfile"
		os.system("ls "+hostsfile);
		break;
	 elif arg == "vi":
		os.system("sudo vim "+hostsfile+sys.argv[i]);
		os.system("sudo chmod 777 "+hostsfile+sys.argv[i]);
		break;
	 elif arg == "cat":
	 	os.system("cat /etc/hosts");
	 elif arg == "-h":
	 	help();
	 elif i>1 and isExists(hostsfile+arg):
	 	os.system("sudo rm -rf /etc/hosts");
	 	os.system("sudo ln -s "+hostsfile+arg+"  /etc/hosts");
	 	# os.system("sudo mv /etc/hosts  "+trace+"temp/");
	 	# os.system("sudo mv "+hostsfile+arg+"  /etc/hosts");
	 	# os.system("sudo mv "+trace+"temp/hosts   " +hostsfile+"lasthosts");
	 	judge();
	 	break;

# if __name__ == '__main__':
#     main(sys.argv);
# os.system("cp /etc/hosts ./");
