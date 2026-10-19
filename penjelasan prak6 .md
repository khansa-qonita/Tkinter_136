`import tkinter as tk` digunakan untuk memanggil library Tkinter yang berfungsi membuat tampilan aplikasi GUI di Python. `as tk` digunakan untuk memberikan nama singkat pada Tkinter supaya lebih mudah dipanggil dalam codingan.

`def prediksi_prodi():` digunakan untuk membuat fungsi bernama `prediksi_prodi`. Di dalamnya terdapat `hasil_label.config()` yang berfungsi mengubah teks pada label hasil menjadi "Prediksi Prodi: Teknologi Informasi" ketika tombol prediksi ditekan. Pada program ini, hasil prediksi masih ditentukan langsung dan belum dipengaruhi oleh nilai yang dimasukkan.

`root = tk.Tk()` digunakan untuk membuat jendela utama aplikasi. `root.title()` berfungsi memberikan judul aplikasi, sedangkan `root.geometry("500x600")` digunakan untuk mengatur ukuran jendela dengan lebar 500 piksel dan tinggi 600 piksel. Selanjutnya, `root.configure(bg="#f0f4f7")` digunakan untuk mengatur warna latar belakang jendela.

`tk.Label()` digunakan untuk menampilkan teks judul aplikasi, yaitu "Aplikasi Prediksi Prodi Pilihan". Bagian `font=("Helvetica", 18, "bold")` mengatur jenis, ukuran, dan ketebalan huruf. `bg` mengatur warna latar belakang, sedangkan `fg` mengatur warna teks. Kemudian, `pack(pady=20)` digunakan untuk menampilkan judul dan memberikan jarak vertikal sebesar 20 piksel.

`tk.Frame(root, bg="#f0f4f7")` digunakan untuk membuat wadah yang menampung komponen input nilai mata pelajaran. Variabel `input_frame` menyimpan frame tersebut, sedangkan `pack(pady=10)` digunakan untuk menampilkan frame dengan jarak vertikal 10 piksel agar tata letak aplikasi lebih rapi.

`entries = []` digunakan untuk membuat list kosong yang akan menyimpan kolom input nilai. Selanjutnya, `for i in range(10)` digunakan untuk melakukan perulangan sebanyak 10 kali sehingga program bisa membuat 10 label mata pelajaran dan 10 kolom input secara otomatis. `tk.Label()` menampilkan tulisan nomor mata pelajaran, sedangkan `tk.Entry()` membuat kolom untuk memasukkan nilai. `grid()` digunakan untuk mengatur posisi label dan kolom input dalam bentuk baris dan kolom. `sticky="w"` membuat label rata kiri, sedangkan `pady` dan `padx` mengatur jarak antarkomponen. Terakhir, `entries.append(entry)` digunakan untuk menyimpan setiap kolom input ke dalam list `entries`.

`tk.Button()` digunakan untuk membuat tombol dengan tulisan "Hasil Prediksi". Bagian `command=prediksi_prodi` berfungsi menghubungkan tombol dengan fungsi prediksi, sehingga fungsi tersebut dijalankan ketika tombol diklik. Kemudian, `pack(pady=20)` digunakan untuk menampilkan tombol dengan jarak vertikal sebesar 20 piksel.

`tk.Label()` digunakan untuk membuat tempat menampilkan hasil prediksi. `text=""` berarti label masih kosong ketika aplikasi pertama kali dibuka. Bagian `font=("Helvetica", 14, "italic")` mengatur jenis, ukuran, dan gaya huruf, sedangkan `bg` mengatur warna latar belakang dan `fg="blue"` membuat teks hasil berwarna biru. `pack(pady=10)` digunakan untuk mengatur posisi label dan jaraknya dari komponen lain.

`root.mainloop()` digunakan untuk menjalankan aplikasi dan menjaga jendela tetap terbuka agar pengguna bisa berinteraksi dengan kolom input dan tombol. Dengan adanya perintah ini, aplikasi dapat terus berjalan sampai jendela ditutup oleh pengguna.

