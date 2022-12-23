import smtplib

server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("mounika.adams@gmail.com","ngcpsoqcpzzfdmei")  #ngcpsoqcpzzfdmei-generated password
server.sendmail("pakhil@gmail.com","Helloooo!!")

server.quit()

