import pywhatkit as pw
import csv

isTeam = int(input("APAKAH NLC ATAU NPC? (1 or 0) : "))
event = str(input("NAMA EVENT? (masukan nama) : "))
team = " perwakilan tim" if isTeam == 1 else ""

try:
    with open(r"C:\\Users\\AL\\Desktop\\python-project\\schematics\\data\\akun\\akun-data.csv", "r", encoding="utf-8") as data :
        read_data = csv.reader(data)
        counter = 1
        for name, number, email, password in read_data :
            name = name.strip()
            number = number.strip()
            if number.startswith('0'):
                number = '+62' + number[1:]
            elif number.startswith('62'):
                number = '+' + number
            email = email.strip()
            password = password.strip()

            msg = '''\
Halo,{tim} {nama}!

Terima kasih telah mendaftar pada acara Schematics {acara}. Pendaftaran a.n {nama} sudah terkonfirmasi. Sebagai salah satu prosedur dalam persiapan perlombaan, mohon mencoba untuk log in ke dalam akun yang telah kami daftarkan pada laman web *schematics-its.com* dengan

Email: *{email_peserta}* 
Password: *{pass_peserta}*

Apabila {nama} telah berhasil log in dengan menggunakan akun tersebut, mohon segera *konfirmasi* kepada kami dan jika terdapat *pertanyaan* atau *kendala* bisa segera hubungi kami.  

Salam,
Kesekretariatan Schematics 2024.

            '''.format(nama=name, tim=team, acara=event, email_peserta=email, pass_peserta=password)
            pw.sendwhatmsg_instantly(number, msg, 20, True, 8)
            print(f"[debug] : {counter}. sending successfully to {name} with {number}")
            counter += 1
except FileNotFoundError:
    print("One or both of the text files are not found.")

except Exception as e:
    print("An error occurred:", str(e))