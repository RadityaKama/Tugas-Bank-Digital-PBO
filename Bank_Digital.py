import datetime

class Nasabah:

    def __init__(self, nama, nomor_rekening, saldo_awal):
        self.nama = nama
        self.nomor_rekening = nomor_rekening
        self.__saldo = saldo_awal
        self._poin_reward = 0
        self._riwayat_transaksi = []
        
        print(f"Halo, {self.nama}! Selamat datang di Bank Cerdas Nusantara!")
        print(f"Akun Anda ({self.nomor_rekening}) telah aktif!")
        self.catat_transaksi("Setoran Awal", saldo_awal, f"Akun dibuka dengan saldo awal")

    def waktu(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def catat_transaksi(self, jenis, nominal, keterangan):
        data_transaksi = {
            "waktu": self.waktu(),
            "jenis": jenis,
            "nominal": nominal,
            "keterangan": keterangan,
            "current_saldo": self.get_saldo(),
            "current_poin": self._poin_reward
        }
        self._riwayat_transaksi.append(data_transaksi)

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo_baru):
        if saldo_baru < 0:
            print("Error! Saldo tidak boleh negatif!")
        else:
            self.__saldo = saldo_baru

    def tampilkan_info(self):
        print("\n--- DATA NASABAH BCN ---")
        print(f"Nama          : {self.nama}")
        print(f"Nomor Rekening: {self.nomor_rekening}")
        self.cek_saldo()
        self.cek_poin()
        print() 

    def cek_saldo(self):
        print(f"Saldo Anda saat ini: Rp{self.get_saldo():,.0f}")

    def cek_poin(self):
        print(f"Poin Reward Anda   : {self._poin_reward} poin")

    def menabung(self, jumlah):
        if jumlah <= 0:
            print("Jumlah tabungan harus positif!")
            return

        cashback = jumlah * 0.01
        
        current_saldo = self.get_saldo()
        self.set_saldo(current_saldo + jumlah)
        print(f"\nBerhasil menabung sebesar Rp{jumlah:,.0f}.")
        self.catat_transaksi("Menabung", jumlah, "Setoran tunai")
        
        saldo_terbaru = self.get_saldo()
        self.set_saldo(saldo_terbaru + cashback)
        print(f"Selamat! Anda mendapat cashback 1% sebesar Rp{cashback:,.0f}.")
        self.catat_transaksi("Cashback", cashback, "Bonus dari setoran")
        
        self.cek_saldo()

    def belanja(self, jumlah, deskripsi):
        if jumlah <= 0:
            print("Jumlah belanja harus positif!")
            return

        current_saldo = self.get_saldo()
        if jumlah > current_saldo:
            print(f"\nMaaf {self.nama}, saldo Anda (Rp{current_saldo:,.0f}) tidak cukup untuk transaksi ini.")
            return

        self.set_saldo(current_saldo - jumlah)
        poin_baru = int(jumlah // 10000)
        self._poin_reward += poin_baru

        print(f"\nPembelanjaan '{deskripsi}' sebesar Rp{jumlah:,.0f} berhasil.")
        if poin_baru > 0:
            print(f"Anda mendapatkan {poin_baru} poin reward baru!")
        
        self.catat_transaksi("Belanja", -jumlah, deskripsi)
        self.cek_saldo()

    def redeem_poin(self, pilihan_hadiah):
        daftar_hadiah = {
            1: {"nama": "Voucher Belanja Rp50.000", "syarat_poin": 100},
            2: {"nama": "Saldo Rp100.000", "syarat_poin": 200},
            3: {"nama": "Smartwatch BCN Edition", "syarat_poin": 500}
        }

        if pilihan_hadiah not in daftar_hadiah:
            print(f"\nPilihan {pilihan_hadiah} tidak ada dalam daftar hadiah!")
            return

        hadiah = daftar_hadiah[pilihan_hadiah]
        biaya_poin = hadiah["syarat_poin"]
        nama_hadiah = hadiah["nama"]

        if self._poin_reward < biaya_poin:
            print(f"\nMaaf, poin Anda ({self._poin_reward}) tidak cukup untuk menukar '{nama_hadiah}'.")
            return

        self._poin_reward -= biaya_poin
        print(f"\nSelamat! Penukaran {biaya_poin} poin dengan '{nama_hadiah}' berhasil.")

        if pilihan_hadiah == 2:
            current_saldo = self.get_saldo()
            self.set_saldo(current_saldo + 100000)
            print("Bonus saldo Rp100.000 telah ditambahkan ke rekening Anda.")
            self.catat_transaksi("Redeem Poin", 100000, "Tukar 200 poin (Saldo)")
        else:
            self.catat_transaksi("Redeem Poin", 0, f"Tukar {biaya_poin} poin ({nama_hadiah})")

        self.cek_poin()

    def generate_riwayat_transaksi(self):
        print("\n\nRIWAYAT TRANSAKSI ANDA")
        print(f"Nasabah: {self.nama} ({self.nomor_rekening})\n")
        
        if not self._riwayat_transaksi:
            print("Belum ada aktivitas transaksi yang tercatat!")
            
        for transaksi in self._riwayat_transaksi:
            print(f"\n[ Waktu: {transaksi['waktu']} ]")
            print(f"  Aktivitas : {transaksi['jenis'].upper()}")
            print(f"  Keterangan: {transaksi['keterangan']}")
            
            if transaksi['jenis'] == 'Redeem Poin' and transaksi['nominal'] == 0:
                 print("  Perubahan: (Penukaran Poin)")
            elif transaksi['nominal'] < 0:
                 print(f"  Perubahan: -Rp{abs(transaksi['nominal']):,.0f}")
            else:
                 print(f"  Perubahan: +Rp{transaksi['nominal']:,.0f}")

            print(f"  Saldo Akhir: Rp{transaksi['current_saldo']:,.0f}")
            print(f"  Poin Akhir : {transaksi['current_poin']} poin")

        print("\n\n--- SALDO AKHIR ---")
        print(f"  Saldo Terkini     : Rp{self.get_saldo():,.0f}")
        print(f"  Poin Reward Total : {self._poin_reward} poin\n")


nasabah1 = Nasabah("Raditya Kama Cahaydewa", "BCN-5240411098", 1000000000)

nasabah1.tampilkan_info()

nasabah1.menabung(10000000)

nasabah1.belanja(45000000, "Beli laptop ThinkPad X1 Carbon Gen 13 Aura Edition")
nasabah1.belanja(2300000, "Beli jersey Manchester United 2025/26 home")
nasabah1.belanja(40000, "Beli kopi")

nasabah1.menabung(50000000)

nasabah1.redeem_poin(3)

nasabah1.generate_riwayat_transaksi()