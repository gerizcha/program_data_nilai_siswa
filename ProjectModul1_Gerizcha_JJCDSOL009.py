nilaiUAS = [
{
    'nama' : 'Selena',
    'kelas' : 'A',
    'jurusan' : 'IPA',
    'nilai' : 50,
    'keterangan' : 'REMEDIAL'
},
{
    'nama' : 'Yesakura',
    'kelas' : 'C',
    'jurusan' : 'IPA',
    'nilai' : 98,
    'keterangan' : 'LULUS'
},
{
    'nama' : 'Yona',
    'kelas' : 'B',
    'jurusan' : 'IPS',
    'nilai' : 60,
    'keterangan' : 'REMEDIAL'
},
{
    'nama' : 'Samantha',
    'kelas' : 'E',
    'jurusan' : 'IPS',
    'nilai' : 64,
    'keterangan' : 'REMEDIAL'
},
{
    'nama' : 'Britney',
    'kelas' : 'D',
    'jurusan' : 'IPA',
    'nilai' : 100,
    'keterangan' : 'LULUS'
}
]

def daftarNilai():
    print('''
                          -----------------------------------------
                          Daftar Nilai UAS Siswa Kelas 12 IPA & IPS
                          -----------------------------------------
                       ''')
    print('\tNo. Index   \t| Nama        \t| Kelas\t| Jurusan    \t| Nilai\t| Keterangan')
    for i in range(len(nilaiUAS)):
        print('\t{}         \t| {}  \t| 12{}\t| {}     \t| {}\t| {}'.format(i,nilaiUAS[i]['nama'],nilaiUAS[i]['kelas'],
        nilaiUAS[i]['jurusan'],nilaiUAS[i]['nilai'],nilaiUAS[i]['keterangan']))

def tambahData():
    print('\n-------------- Silakan Bapak/Ibu Guru isi keterangan di bawah ini --------------\n')
    
    while True:
        namaSiswa = input('\nKetikkan Nama Siswa : ').capitalize()
        if namaSiswa == '' or namaSiswa.isalpha() == False:
            print("\n\t\t\t** Nama siswa tidak boleh kosong atau berisi angka/simbol, silakan ketikkan Nama yang benar! **\n")
        else:
            break
    
    kelas = ('A', 'B', 'C', 'D', 'E')
    while True:
        kelasSiswa = input('\nKetikkan Kelas Siswa : 12 ').upper()
        if kelasSiswa in kelas:
            break
        else:
            print("\n\t\t\t** Kelas tidak boleh kosong dan hanya di antara A sampai E, silakan ketikkan Kelas yang benar! **\n")
    
    jurusan = ('IPA', 'IPS')
    while True:
        jurusanSiswa = input('\nJurusan IPA/IPS? ').upper()
        if jurusanSiswa in jurusan:
            break
        else:
            print("\n\t\t\t** Jurusan tidak boleh kosong dan hanya ada IPA/IPS, silakan ketikkan Jurusan yang benar! **\n")

    while True:
        while True:
            nilai= input('\nKetikkan nilai siswa: ')
            if nilai.isnumeric() == True:
                break
            else:
                print("\n\t\t\t** Nilai harus ANGKA di antara 0-100, silakan ketikkan Nilai yang benar! **\n")
        
        nilaiSiswa = int(nilai)
        if nilaiSiswa >= 0 and nilaiSiswa <= 100:
            break
        else:
            print("\n\t\t\t** Nilai harus ANGKA di antara 0-100, silakan ketikkan Nilai yang benar! **\n")

    while True:
        while True:
            keterangan = input('''
** Ketik angka 1 = LULUS
** Ketik angka 2 = REMEDIAL

Berdasarkan Nilai, apakah siswa LULUS atau REMEDIAL? ''')

            if keterangan == '1' or keterangan == '2':
                break
            else:
                print("\n\t\t\t** Ketik angka 1 atau angka 2 saja, silakan ketikkan Angka yang benar! **\n")
        
        keteranganNilai = int(keterangan)
        if keteranganNilai == 1:
            keteranganNilai = 'LULUS'
            break
        elif keteranganNilai == 2:
            keteranganNilai = 'REMEDIAL'
            break


    nilaiUAS.append({
        'nama': namaSiswa,
        'kelas' : kelasSiswa,
        'jurusan' : jurusanSiswa,
        'nilai' : nilaiSiswa,
        'keterangan' : keteranganNilai
    })
    daftarNilai()
    print('\n\n\t--- Data baru sudah berhasil ditambahkan ke dalam Daftar Nilai UAS Siswa. Silakan Bapak/Ibu Guru cek kembali. ---')

def ubahData():
    daftarNilai()

    while True:
        while True:
            ubahAbsen= input('\n\n\tBapak/Ibu Guru ingin MENGUBAH data siswa dengan No. Index : ')
            if ubahAbsen.isnumeric() == True:   
                noAbsen = int(ubahAbsen)
                if noAbsen>= len(nilaiUAS):
                    print("\n\n\t\t** Tidak ada siswa dengan No. Index tersebut. Silakan Bapak/Ibu Guru ketik angka lain. **\n")
                else:
                    break
            else:
                print("\n\n\t\t** Tidak ada siswa dengan No. Index tersebut. Silakan Bapak/Ibu Guru ketik angka lain. **") 


        print('\n\n\tBerikut adalah data siswa tersebut:\n\n\t-----------------------------------------------------------------------------')
        print('\tNo. Index   \t| Nama        \t| Kelas\t| Jurusan    \t| Nilai\t| Keterangan')
        for i in range(len(nilaiUAS)):
            if i == noAbsen:
                print('\t{}         \t| {}  \t| 12{}\t| {}     \t| {}\t| {}'.format(i,nilaiUAS[i]['nama'],nilaiUAS[i]['kelas'],
                nilaiUAS[i]['jurusan'],nilaiUAS[i]['nilai'],nilaiUAS[i]['keterangan']))
            else:
                i+= 1
        print('''
       
        *** KATEGORI 1: Nama | 2: Kelas | 3: Jurusan | 4: Nilai | 5: Keterangan ***

        ''')
        while True:
            ubah = input('\tKetik angka Kategori yang ingin Bapak/Guru ubah dari data siswa tersebut : ')
            if ubah == '1':
                ubahKategori = input('\n\tKetikkan NAMA baru yang akan diupdate ke database: ')
                if ubahKategori == '' or ubahKategori.isalpha() == False:
                    print("\n\t\t\t** Nama siswa tidak boleh kosong atau berisi angka, silakan ketikkan Nama yang benar! **\n")
                else:
                    nilaiUAS[noAbsen]['nama'] = ubahKategori.capitalize()
                    break

            elif ubah == '2':
                kelas = ('A', 'B', 'C', 'D', 'E')
                ubahKategori = input('\n\tKetikkan KELAS baru yang akan diupdate ke database : 12 ').upper()
                if ubahKategori not in kelas:
                    print("\n\t\t\t** Kelas tidak boleh kosong dan hanya di antara A sampai E, silakan ketikkan Kelas yang benar! **\n")
                else:
                    nilaiUAS[noAbsen]['kelas'] = ubahKategori
                    break

            elif ubah == '3':
                jurusan = ('IPA', 'IPS')
                ubahKategori = input('\n\tKetikkan JURUSAN baru yang akan diupdate ke database (IPA/IPS): ').upper()
                if ubahKategori not in jurusan:
                    print("\n\t\t\t** Jurusan hanya ada IPA/IPS, silakan ketikkan Jurusan yang benar! **\n")
                else:
                    nilaiUAS[noAbsen]['jurusan'] = ubahKategori.upper()
                    break

            elif ubah == '4':
                while True:
                    ubahKategori= input('\n\tKetikkan NILAI baru siswa yang akan diupdate ke database: ')
                    if ubahKategori.isnumeric() != True:
                        print("\n\t\t\t** Nilai harus ANGKA di antara 0-100, silakan ketikkan Nilai yang benar! **\n")
                    else:
                        break 

                nilaiSiswa = int(ubahKategori)
                if nilaiSiswa > 0 and nilaiSiswa <= 100:
                    nilaiUAS[noAbsen]['nilai'] = nilaiSiswa
                    break
                else:
                    print("\n\t\t\t** Nilai harus ANGKA di antara 0-100, silakan ketikkan Nilai yang benar! **\n")

            elif ubah == '5':
                while True:
                    keterangan = input('''
        ** Ketik angka 1 = LULUS
        ** Ketik angka 2 = REMEDIAL

        Berdasarkan Nilai, apakah siswa LULUS atau REMEDIAL? ''')

                    if keterangan.isnumeric() == True and keterangan == '1' or keterangan == '2':
                        break
                    else:
                        print("\n\t\t\t** Ketik angka 1 atau angka 2 saja, silakan ketikkan Angka yang benar! **\n")
                keteranganNilai = int(keterangan)
                if keteranganNilai == 1:
                    nilaiUAS[noAbsen]['keterangan'] = 'LULUS'
                    break
                elif keteranganNilai == 2:
                    nilaiUAS[noAbsen]['keterangan'] = 'REMEDIAL'
                    break
            elif ubah == '' or ubah.isnumeric() == False or int(ubah) > 5:
                print('''
       
        - - KATEGORI 1: Nama | 2: Kelas | 3: Jurusan | 4: Nilai | 5: Keterangan - -

        ''')
                print('\t\t** Pilihan hanya di antara angka 1 sampai 5 saja. Silakan ketik angka Kategori yang diinginkan. **\n')

        daftarNilai()
        print('\n\t--- Data yang baru sudah berhasil ter-update ke dalam Daftar Nilai UAS Siswa. Silakan Bapak/Ibu Guru cek kembali. ---')
        break

def hapusData():
    daftarNilai()

    while True:
        while True:
            absen= input('\n\n\tBapak/Ibu Guru ingin MENGHAPUS data siswa dengan No. Index : ')
            if absen.isnumeric() == True:   
                noAbsen = int(absen)
                if noAbsen >= len(nilaiUAS):
                    print("\n\n\t\t** No. Index harus ANGKA yang terdapat dalam daftar, silakan ketikkan Angka yang benar! **\n")
                else:
                    break
            else:
                print("\n\n\t\t** No. Index harus ANGKA yang terdapat dalam daftar, silakan ketikkan Angka yang benar! **\n") 


        while True:
            sureNot = input('\n\n\tPERHATIAN! Apakah Bapak/Ibu Guru yakin untuk menghapus data siswa tersebut? (Y/N)  ').upper()
            if sureNot == 'Y':
                del nilaiUAS[noAbsen]
                daftarNilai()
                print('\n\n\t--- Data sudah berhasil dihapus. Silakan Bapak/Ibu Guru cek kembali. ---')
                break
            elif sureNot == 'N' :
                daftarNilai()
                print('\n\n\t--- Data tidak jadi dihapus. Silakan Bapak/Ibu Guru cek kembali. ---')
                break
            elif sureNot != 'Y' or sureNot!= 'N':
                print("\n\n\t\t** Ketik Y atau N saja, silakan Bapak/Ibu Guru input huruf yang benar! **\n")
        break


while True:
    pilihanMenu = input('''
    ***
    
    Salam sejahtera Bapak/Ibu Guru, selamat datang di Database Nilai UAS Siswa Kelas 12 IPA & IPS
    
    Pilihan:
    1. Daftar Nilai Siswa
    2. MENAMBAH Data Nilai
    3. MENGUBAH Data Nilai
    4. MENGHAPUS Data Nilai
    5. Keluar dari Database

    Silakan ketik angka dalam Pilihan 1-5 : ''')

    if(pilihanMenu=='1') :
        daftarNilai()
    elif(pilihanMenu=='2'):
        tambahData()
    elif(pilihanMenu=='3'):
        ubahData()
    elif(pilihanMenu=='4'):
        hapusData()
    elif(pilihanMenu=='5'):
        print('''
    **

    Terima kasih Bapak/Ibu Guru sudah mengakses database Nilai UAS Siswa Kelas 12 IPA & IPS.
    Jika ada kesulitan dalam menggunakan program ini, silakan hubungi staf IT sekolah.
    Kami siap membantu.
    Sampai jumpa!
    
    **
    
    ''')
        break