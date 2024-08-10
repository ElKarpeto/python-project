import pywhatkit as pw
import csv

try:
    with open(r"C:\\Users\\AL\\Desktop\\python-project\\schematics\\data\\data.csv", "r", encoding="utf-8") as data :
        read_data = csv.reader(data)
        counter = 1
        for name, number in read_data :
            name = name.strip()
            number = number.strip()
            if number.startswith('0'):
                number = '+62' + number[1:]
            elif number.startswith('62'):
                number = '+' + number

            msg = '''\
Halo, {nama}!

Terima kasih telah mendaftar pada acara Schematics BST SEMINAR. Kami mendapati kesalahan data pada kurangnya data *email*. Dimohon untuk dapat mengirimkan kembali data-data tersebut dengan membalas WA ini agar kami dapat memverifikasi pendaftaran atas nama {nama}.

Apabila terdapat pertanyaan atau kendala bisa segera hubungi kami.  

Salam,
Kesekretariatan Schematics 2024.
            '''.format(nama=name)
            pw.sendwhatmsg_instantly(number, msg, 20, True, 8)
            print(f"[debug] : {counter}. sending successfully to {name} with {number}")

except FileNotFoundError:
    print("One or both of the text files are not found.")

except Exception as e:
    print("An error occurred:", str(e))