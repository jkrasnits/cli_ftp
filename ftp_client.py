import ftplib
import sys

loop_var = True

if len(sys.argv) == 4:
	arg_list = str(sys.argv)
	print "-------------------------------------------------------------"
	print "Server --->" + sys.argv[1]
	print "Username --->" + sys.argv[2]
	print "Password --->" + sys.argv[3]
	print "-------------------------------------------------------------"
	ftp = ftplib.FTP(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]))
else: 
	if (not len(sys.argv) == 1) and (not len(sys.argv) == 4):
		print "Incorrect number of arguments"

	while loop_var:
		print "Python FTP Client\n"
		ftp_server = raw_input("Server: ")
		ftp_user = raw_input("Username: ")
		ftp_password = raw_input("Password: ")
		try:
		    ftp = ftplib.FTP(ftp_server, ftp_user, ftp_password)
		    print "connection successful"
		    loop_var = False
		except Exception,e:
		    print e
		    print "try again"
print "------------------------------------------------------------------"
print ftp.getwelcome();
print ftp.retrlines('LIST')
print "------------------------------------------------------------------"
print "\n"

print "\nls "
print "cwd"
print "mkdir"
print "rmd"
print "delete"
print "help"
print "rename"
print "\nquit"

while True:
    command = raw_input("ftp> ")
    
    if command == "ls":
		print "------------------------------------------------------------------"
		print ftp.retrlines('LIST')
		print "------------------------------------------------------------------"
		print "\n"

    elif command == "cwd":
        cd = raw_input("To: ")
        ftp.cwd(cd)
        print "Directory change successful."

    elif command == "mkdir":
        mkdir = raw_input("Choose a name for your directory: ")
        ftp.mkd(mkdir)
        print "Directory %s created." % mkdir

    elif command == "rmd":
        rm = raw_input("What directory to remove? ")
        safe_rm = raw_input("Are you sure you want to remove directory \"%s\" from the server? (y/n) " % rm)
        if safe_rm == "y":
            ftp.rmd(rm)
            print "Directory removed successfully."
        if safe_rm == "n":
            print "Directory not removed."
        else:
            print "Invalid command"

    elif command == "rename":
        ren_orig = raw_input("File or folder to rename: ")
        ren_new = raw_input("New name: ")
        ftp.rename(ren_orig,ren_new)
        print "%s was successfully renamed to %s." % (ren_orig, ren_new)

    elif command == "delete":
        del_file = raw_input("File to delete: ")
        ftp.delete(del_file)
        print "%s was successfully deleted." % (del_file)

    elif command == "quit":
        ftp.quit
        sys.exit(0)
        
    elif command == "help":
        print "\nls"
        print "cwd"
        print "mkdir"
        print "rmd"
        print "delete"
        print "help"
        print "rename"
        print "get (NOT YET ADDED)"
        print "mget (NOT YET ADDED)"
        print "put (NOT YET ADDED)"
        print "mput (NOT YET ADDED)"
        print "\nquit"

    else:
    	print "command not recognized"