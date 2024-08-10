import smtplib
import ssl
from email.message import EmailMessage 
from email.mime.base import MIMEBase
from email import encoders
import csv

email_sender = 'data.schematics24@gmail.com' #email sch (cek deskripsi)
email_password = 'gawevchaudezturk' #pwd bot sch (cek desripsi)

csv_path = r'C:\\Users\\AL\\Desktop\\python-project\\schematics\\data\\data.csv' # lokasi file kalian
with open(csv_path, "r", encoding="utf-8") as data :
    read_data = csv.reader(data)
    subject = 'Permintaan Nomor Telepon untuk data Schematics yang kurang lengkap' #ganti sesuai yang ad di docs

    # Iterate through the CSV data
    counter = 1
    for email, nama in read_data:
        email_receiver = email.strip()
        nickname = nama.strip()
        # attachment_file_name_1 = r"C:\\Users\\AL\\Desktop\\python-project\\schematics\\data\\sounding-bst\\Guidebook Advance BST.pdf"
        # attachment_file_name_2 = r"C:\\Users\\AL\\Desktop\\python-project\\schematics\\data\\sounding-bst\\Guidebook Basic BST.pdf"
        
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject

        # ubah bagian bawah ini sesuai yang ada di docs juga
        body = f'''<html>
    <body>
        Halo, {nickname}!<br />

        Terima kasih telah mendaftar pada acara
        <strong>Schematics BST SEMINAR</strong>. Pendaftaran atas nama
        {nickname} telah terkonfirmasi. Namun, kami mendapati kesalahan data
        pada Nomor Whatsapp (tidak valid).
        <br />
        Dimohon untuk dapat mengirimkan kembali data-data tersebut dengan
        korfirmasi melalui Whatsapp
        <strong
            ><a href="https://wa.me/6289658857422"
                >089658857422 (Miski)</a
            ></strong
        >
        ini agar kami dapat memverifikasi pendaftaran atas nama {nickname}.<br />

        Apabila terdapat pertanyaan atau kendala bisa segera hubungi kami.
        <br />

        Salam, <br />
        Kesekretariatan Schematics 2024
    </body>
</html>
        '''.format(nickname=nickname)
        # Make the message multipart for HTML content and attachments
        em.add_alternative(body, subtype='html')

        # with open(attachment_file_name_1, 'rb') as attachment_file_1:
        #     file_data_1 = attachment_file_1.read()
        #     # file_name_1 = attachment_file_1.name.split("/")[-1]
        #     attachment1 = MIMEBase('application', 'octet-stream')
        #     attachment1.set_payload(file_data_1)
        #     encoders.encode_base64(attachment1)
        #     attachment1.add_header('Content-Disposition', f'attachment; filename="Guidebook Advance BST.pdf"')
        #     em.attach(attachment1)

        # # Attach the second file
        # with open(attachment_file_name_2, 'rb') as attachment_file_2:
        #     file_data_2 = attachment_file_2.read()
        #     attachment2 = MIMEBase('application', 'octet-stream')
        #     attachment2.set_payload(file_data_2)
        #     encoders.encode_base64(attachment2)
        #     attachment2.add_header('Content-Disposition', f'attachment; filename="Guidebook Basic BST.pdf"')
        #     em.attach(attachment2)

        context = ssl.create_default_context()
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
            print(f"[debug] : {counter}. send e-mail to {nama} with {email}")
        counter += 1