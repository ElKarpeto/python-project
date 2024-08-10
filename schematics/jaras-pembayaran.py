import pywhatkit as pw
import csv

isTeam = int(input("APAKAH NLC ATAU NPC? (1 or 0) : "))
event = str(input("NAMA EVENT? (masukan nama) : "))
team = " perwakilan tim" if isTeam == 1 else ""

try:
    with open(r"C:\Users\AL\Desktop\python-project\schematics\data\pembayaran\data-pembayaran.csv", "r", encoding="utf-8") as data :
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
Halo,{tim} {nama}!

Terima kasih telah mendaftar pada acara Schematics {acara}. Pendaftaran a.n {nama} sudah terkonfirmasi. Stay tuned terkait informasi lebih lanjut mengenai kelengkapan berkas yang akan digunakan. 

Apabila terdapat pertanyaan atau kendala bisa segera hubungi kami.

Salam,
Kesekretariatan Schematics 2024.
            '''.format(nama=name, tim=team, acara=event)
            pw.sendwhatmsg_instantly(number, msg, 20, True, 8)
            
            print(f"[debug] : {counter}. sending successfully to {name} with {number}")
            counter += 1
except FileNotFoundError:
    print("One or both of the text files are not found.")

except Exception as e:
    print("An error occurred:", str(e))