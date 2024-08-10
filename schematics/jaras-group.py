import pywhatkit as pw
import csv

isTeam = int(input("APAKAH NLC ATAU NPC? (1 or 0) : "))
team = " perwakilan tim" if isTeam == 1 else ""

try:
    with open(r"C:\Users\AL\Desktop\python-project\schematics\data\group\data-group.csv", "r", encoding="utf-8") as data :
        counter = 1
        read_data = csv.reader(data)
        for name, number in read_data :
            name = name.strip()
            number = number.strip()
            if number.startswith('0'):
                number = '+62' + number[1:]
            elif number.startswith('62'):
                number = '+' + number
            msg = '''\
Halo, {tim} {nama}!

Terima kasih sudah mendaftar pada acara Schematics NLC. Pembayaran sudah berhasil diverifikasi. *Perwakilan ketua tim* diharapkan untuk join group WhatsApp melalui link yang kami kirim di bawah ini *sesuai dengan region tim mendaftar*. Stay tuned terkait informasi lebih lanjut mengenai pemberian akun Schematics NLC dan kelengkapan berkas yang akan digunakan.

Apabila terdapat pertanyaan atau kendala bisa segera hubungi kami.

Salam,
Kesekretariatan Schematics 2024.

Online: https://chat.whatsapp.com/CJI4G2SGpNQLLRNCf8H3PZ
Mojokerto: https://chat.whatsapp.com/HGsvCsY9ocLAqyu1EEdxl7
Sampang: https://chat.whatsapp.com/EPejzm0Glsu1d28Zk1v51n
Malang: https://chat.whatsapp.com/FkIlrvvT58iKShkkeh8JUp
Kediri: https://chat.whatsapp.com/HSBdgcpK1bABfiBigJSIJS
Jember: https://chat.whatsapp.com/DRDb8GQPROn88pdYOvXlbD
Jakarta: https://chat.whatsapp.com/IxlyiQBYIrJLUSYKP1fjzG
Surabaya: https://chat.whatsapp.com/Ff63gPVgiOdG1YxTv26KJA

            '''.format(nama=name, tim=team)
            pw.sendwhatmsg_instantly(number, msg, 25, True, 10)
            
            print(f"[debug] : {counter}. sending successfully to \"{name}\" with {number}")
            counter += 1
except FileNotFoundError:
    print("One or both of the text files are not found.")

except Exception as e:
    print("An error occurred:", str(e))