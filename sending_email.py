import smtplib 
#============================================
a = input(' [+]Enter sender email -->')
b = input(' [+]Enter sender password -->')
x = input(' [+]Enter recevier email -->')
y = input(' [+]Enter your message here -->')
#============================================
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
s.login(a, b) 
#=======================================
message = y
#=======================================
s.sendmail(a, x, message) 
s.quit() 

