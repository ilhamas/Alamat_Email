def nama_email(alamat):                   #membuat fungsi dengan bernama nama_email
    list1 = alamat.split('@')             #membuat list untuk mensplit parameter yang dimasukan dengan separator @
    list2 = list1[1]                      #membuat list berisi index ke 0 list1
    list3 = list2.split('.')              #membuat list untuk mensplit list3 dengan separator titik
    
    user_salah=['!','#','$','%','^','&','*',')','(','-','=','+','{','[','}',']','>',':',';','<','/','?',','] #list berisi tanda yang dilarang
    namaUser = list1[0]   #membuat variabel nama user berdasarkan index ke 0 list 1
    for i in namaUser:    #membuat loop untuk memeriksa apakah nama user sesuai pengecualian di soal
        if i in user_salah:   #membuat kondisi apakah elemen pada list nama user sesuai soal atau tidak
            print('Hasil: Email Tidak valid!! Format Email Salah!!') #jika tidak sesuai print sebagai berikut

    hosting_salah=['_','!','#','$','%','^','&','*',')','(','-','=','+','{','[','}',']','>',':',';','<','/','?',','] #tanda yang dilarang
    namaHosting=list3[0]   #membuat variabel namaHosting berdasarkan index ke 0 list 3
    for i in namaHosting:  #membuat loop untuk memeriksa apakah nama hosting sesuai syarat di soal
        if i in hosting_salah: #membuat kondisi apakah elemen pada list nama hosting sesuai soal atau tidak
            print('Hasil : Email Tidak valid!! Format Email Salah!!') #jika tidak sesuai print sebagai berikut
    
    ekstensi_salah=['1','2','3','4','5','6','7','8','9','0','_','!','#','$','%','^','&','*',')','(','-','=','+','{','[','}',']','>',':',';','<','/','?',','] #tanda yang dilarang
    ekstensi = list3[1] #membuat variabel ekstensi berdasarkan index ke 1 list 3
    for i in ekstensi:  #membuat loop untuk memeriksa apakah nama hosting sesuai syarat di soal
        if i in ekstensi_salah or (len(ekstensi))>=5 : #membuat kondisi apakah elemen pada list ekstensi sesuai soal atau tidak
            print('Hasil : Email Tidak valid!! Format Email Salah!!') #jika tidak sesuai print sebagai berikut
            
    print('Jika Tidak Muncul Tulisan Email Tidak valid!! Format Email Salah!!, Maka Hasil Sebenarnya : Alamat Email Yang Anda Masukkan Valid!!')
nama_email('ilhamuta@gmail.com')