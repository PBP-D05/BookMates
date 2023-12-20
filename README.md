Citra Andini Hermawan - **2206830012** <br>
Dian Fathur Rahman - **2206082096** <br>
Eryawan Presma Yulianrifat - **2206041335** <br>
Ellisha Natasha - **2206028516** <br>
Joy Debora Sitorus - **2206082991** <br>
Veronica Kylie - **2206029563** <br>

---

# Aplikasi yang diajukan
Kelompok kami berencana untuk mengembangkan sebuah aplikasi **inventori buku** untuk **anak-anak**. Aplikasi ini akan mencakup **katalog buku** yang **lengkap** serta fitur **komunitas** untuk meningkatkan motivasi anak untuk membaca. Pada komunitas ini, terdapat pengguna yang bisa memberikan **tantangan membaca** bagi anggota komunitas lainnya. Ketika menyelesaikan sebuah tantangan, pengguna akan **memperoleh poin** yang dapat dimanfaatkan untuk menaikkan peringkat *leaderboard*. Dengan **desain yang cerah** dan **menarik** yang secara khusus dirancang untuk **anak-anak**, kami berharap aplikasi ini akan **meningkatkan minat membaca** di kalangan **anak-anak**, dengan tujuan akhir **meningkatkan tingkat literasi** di masyarakat Indonesia kedepannya.

# Manfaat Aplikasi:;/

1. **Peningkatan Kesukaan Membaca**

Aplikasi ini memberikan pengalaman membaca yang menyenangkan melalui komunitas dan challenge menarik. Aplikasi ini juga dilengkapi tampilan yang berwarna dan menarik, merangsang kesukaan anak-anak terhadap membaca.

2. **Fasilitas Pencarian yang Mudah**

Dengan katalog buku yang lengkap dan fitur *search* katalog, pengguna dapat dengan mudah mencari buku yang mereka inginkan, memperkaya pengalaman membaca mereka.

3. **Pembangunan Komunitas Membaca** 

Aplikasi ini memfasilitasi pembentukan komunitas membaca di kalangan anak-anak, memungkinkan mereka berbagi pengalaman membaca dan merekomendasikan buku satu sama lain. Komunitas diharapkan dapat memberikan rasa kebersamaan dan *sense of purpose*.

4. **Literasi yang Menyenangkan** 

Dengan tantangan membaca dan leaderboard, aplikasi ini menjadikan pembelajaran membaca sebagai pengalaman yang menyenangkan dan kompetitif, memotivasi anak-anak untuk membaca lebih banyak dan lebih sering.

# Daftar modul yang akan diimplementasikan
1. **Login & Register**. Halaman untuk user registrasi akun (bila belum punya) atau login jika sudah punya akun. Adapula akun user dapat berupa pengguna biasa maupun guru.

2. **Dashboard user & Sidebar**. Halaman yang menampilkan profil pengguna, *history* buku yang telah dibaca, dan komunitas dimana ia tergabung. Jika ia merupakan seorang guru, maka akan ada tombol untuk mengarahkan ke halaman untuk mengelola buku yang diunggah. Selain itu, sidebar berperan seperti navbar yang akan memungkinkan pengguna pindah ke halaman lainnya. 

3. **Komunitas antara guru dan anak-anak**. Pada modul ini pengguna yang memiliki *role* sebagai guru dapat membuat komunitas dan pengguna dengan *role* anak-anak dapat bergabung ke komunitas yang mereka inginkan. Dalam sebuah komunitas, seorang guru dapat memberikan tantangan membaca kepada anak-anaknya.

4. **Challenge + leaderboard**. Modul ini memungkinkan pengguna untuk mengikuti tantangan membaca (*challenges*) yang akan dibuat oleh *role* guru dan melihat peringkat pengguna lainnya dalam leaderboard. Modul ini menciptakan pengalaman belajar yang kompetitif dan menyenangkan, memotivasi anak-anak untuk membaca lebih banyak buku.

5. **Search katalog**. Modul ini menampilkan katalog-katalog buku yang dikelompokkan berdasarkan genre dan penulis buku. Halaman web ini juga dilengkapi dengan fitur search atau pencarian di mana user dapat melakukan pencarian dalam bentuk tag umur maupun nama penulis. Hasil pencarian akan menampilkan buku-buku yang sesuai dengan permintaan user.

6. **Mengelola buku**. Modul dimana seseorang dengan role *guru* dapat menambahkan dan menghapus buku yang telah ditambahkan oleh guru. Page yang dibuat dalam modul ini akan menampilkan buku-buku yang telah dimasukkan oleh guru tersebut dalam bentuk *card* dan menampilkan detil lebih lanjut mengenai buku tersebut jika button pada card diklik. Buku yang ditambahkan guru dapat dilihat oleh semua pengguna aplikasi, tidak terbatas ke komunitas tersebut.

# Sumber dataset
[Kaggle 1000 Children Books on Amazon](https://www.kaggle.com/datasets/modhiibrahimalmannaa/1000-children-books-on-amazom/)

# Role Pengguna

## Guru

- Membuat sebuah komunitas/kelas
- Menambahkan buku baru dalam katalog
- Menghapus buku yang ia ditambahkan sebelumnya
- Memberi challenge bagi anggota komunitas
- Melakukan hal-hal yang dilakukan pengguna biasa

## Pengguna biasa

- Explore buku baru yang dapat dibaca baik melalui katalog maupun rekomendasi
- Menjadi anggota dalam komunitas buku
- Berpartisipasi dalam leaderboard dengan menyelesaikan berbagai challenge
- Mengakses dashboard untuk melihat progressnya
