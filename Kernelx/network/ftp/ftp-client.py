from ftplib import FTP
ftp = FTP('89.219.32.27')
ftp.login(user='testuser',passwd='12345')
data = ftp.retrlines('LIST')
cur = ftp.pwd()
print(cur)
print(data)
