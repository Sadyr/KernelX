from ftplib import FTP

ftp = FTP('')
ftp.connect("localhost", 1026)
ftp.login()
ftp.cwd('/home/balerion/Downloads')
ftp.retrlines('LIST')


def uploadfile():
    filename = '/home/balerion/Documents/testfile.txt'
    ftp.storbinary('STOR ' + filename, open(filename, 'rb'))
    ftp.quit()


def downloadfile():
    filename = '/home/balerion/downloadfile.txt'
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    ftp.quit()
    localfile.close()


uploadfile()
