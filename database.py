import sqlite3 
from modals.userInfo import UserInfo

class db_Helper:
    def __init__(self) -> None:
    # Veritabanına bağlanma
        self.conn = sqlite3.connect('veritabani.db')
        self.cursor = self.conn.cursor()
        self.tablolariOlustur()

    # görev durumu (tamamlanacak: 0, devam ediyor: 1, tamamlandi: 2 )
    def tablolariOlustur(self) :
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS kullanicilar (  
            kullaniciID INTEGER PRIMARY KEY AUTOINCREMENT,  
            kullaniciAdi TEXT,  
            kullaniciSoyadi TEXT,    
            kullaniciMail TEXT,
            kullaniciSifre TEXT
        )
        ''')
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS calisanlar (  
            calisanID INTEGER PRIMARY KEY AUTOINCREMENT,  
            kullaniciID INTEGER,  
            calisanAdi TEXT,  
            calisanSoyadi TEXT,  
            calisanMail TEXT,   
            zamanindaTamamlananGorevlerMiktari INTEGER,   
            zamanindaTamamlanamayanGorevlerMiktari INTEGER
        )
        ''')
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS projeler (  
            projeID INTEGER PRIMARY KEY AUTOINCREMENT,  
            kullaniciID INTEGER,  
            projeAdi TEXT, 
            projeAciklama TEXT,
            baslangicTarihi DATE,  
            bitisTarihi DATE,
            gecikmeMiktari INTEGER
        )
        ''')
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS gorevler (  
            gorevID INTEGER PRIMARY KEY AUTOINCREMENT,  
            projeID INTEGER,  
            calisanID INTEGER,
            gorevAdi TEXT,
            gorevAciklama TEXT,
            baslangicTarihi DATE,
            bitisTarihi DATE,
            gorevDurum INTEGER,                   
            adamGunDegeri INTEGER,
            gecikmeMiktari INTEGER
        )
        ''')
        self.conn.commit()

    def kullaniciEkle(self, UserInfo) :
        self.cursor.execute('''
        INSERT INTO kullanicilar(
            kullaniciAdi,
            kullaniciSoyadi,
            kullaniciMail,
            kullaniciSifre
        )
        VALUES(?, ?, ?, ?)
        ''', (UserInfo.kullaniciAdi, UserInfo.kullaniciSoyadi, UserInfo.kullaniciMail, UserInfo.kullaniciSifre))
        self.conn.commit()
        
    # kullanıcı kişisel bilgileri
    def kullaniciKisiselBilgilari(self, kullaniciMail) :
        self.cursor.execute('''
        SELECT 
            kullaniciID,
            kullaniciAdi,
            kullaniciSoyadi,
            kullaniciMail,
            kullaniciSifre          
        FROM
            kullanicilar
        WHERE
            kullaniciMail = ?
        ''', (kullaniciMail,))
        self.conn.commit()
        userList = self.cursor.fetchall()
        return userList 
        
    # isme soyada göre kullanıcı silme 
    def kullaniciSil(self, ad, soyad) :
        self.cursor.execute('''
        DELETE
        FROM
            kullanicilar
        WHERE
            kullaniciAdi = ? AND kullaniciSoyadi = ?
        ''', (ad, soyad,))
        self.conn.commit()

    # ID'ye göre kullanıcı silme 
    def kullaniciSilID(self, kulID) :
        self.cursor.execute('''
        DELETE
        FROM
            kullanicilar
        WHERE
            kullaniciID = ?
        ''', (kulID,))
        self.conn.commit()











    # çalışan eklerken ilk başta hiç bir görevi olmadığı için hepsine sıfır atıyoruz
    def calisanEkle(self, kulID, calAdi, calSoyadi, calMail) :
        self.cursor.execute('''
        INSERT INTO calisanlar(
        kullaniciID,
        calisanAdi,
        calisanSoyadi,
        calisanMail,
        zamanindaTamamlananGorevlerMiktari,
        zamanindaTamamlanamayanGorevlerMiktari
        )
        VALUES(?, ?, ?, ?, ?, ?)
        ''', (kulID, calAdi, calSoyadi, calMail, 0, 0,))
        self.conn.commit()

    # bütün çalışanları döndürür
    def calisanKisiselBilgilari(self) :
        self.cursor.execute('''
        SELECT
            calisanID,
            kullaniciID,
            calisanAdi,
            calisanSoyadi,
            calisanMail,
            zamanindaTamamlananGorevlerMiktari,
            zamanindaTamamlanamayanGorevlerMiktari
        FROM
            calisanlar
        WHERE
            1
        ''')
        self.conn.commit()

    # çalışana ait zamanında tamamlanan görevleri güncelleme
    def calisanZamanindaTamamlananGuncelleme(self, zamaninda, calID, kulID) :
        self.cursor.execute('''
        UPDATE
            calisanlar
        SET
            zamanindaTamamlananGorevlerMiktari = ?
        WHERE
            calisanID = ? AND kullaniciID = ?
        ''', (zamaninda, calID, kulID,))
        self.conn.commit()

    # çalışana ait zamanında tamamlanmayan görevleri güncelleme
    def calisanZamanindaOlmayanGuncelleme(self, zamanindaOlmayan, calID, kulID) :
        self.cursor.execute('''
        UPDATE
            calisanlar
        SET
            zamanindaTamamlanamayanGorevlerMiktari = ?
        WHERE
            calisanID = ? AND kullaniciID = ?
        ''', (zamanindaOlmayan, calID, kulID,))
        self.conn.commit()

    # isme soyada göre çalışan silem
    def calisanSil(self, ad, soyad) :
        self.cursor.execute('''
        DELETE
        FROM
            calisanlar
        WHERE
            calisanAdi = ? AND calisanSoyadi = ?
        ''', (ad, soyad,))
        self.conn.commit()

    # ID'ye göre çalışan silem
    def calisanSilID(self, calID) :
        self.cursor.execute('''
        DELETE
        FROM
            calisanlar
        WHERE
            calisanID = ?
        ''', (calID,))
        self.conn.commit()











    # proje eklerken ilk başta gecikme miktarını 0 ve zamanında tamamlandıyı true olarak atıyorum
    def projeEkle(self, kulID, projeAdi, projeAciklama, basTarihi, bitTarihi) :
        self.cursor.execute('''
        INSERT INTO projeler(
            kullaniciID,
            projeAdi,
            projeAciklama,
            baslangicTarihi,
            bitisTarihi,
            gecikmeMiktari,
        )
        VALUES(?, ?, ?, ?, ?, ?)
        ''', (kulID, projeAdi, projeAciklama, basTarihi, bitTarihi, 0,))
        self.conn.commit()

    # projenin bilgilerini görüntülemek için bir fonksiyondur
    def projeDetaySayfasi(self, projeID) :
        self.cursor.execute('''
        SELECT
            projeAdi,
            projeAciklama,
            baslangicTarihi,
            bitisTarihi,
            gecikmeMiktari
        FROM
            projeler
        WHERE
            projeID = ?
        ''', (projeID,))
        self.conn.commit()

    # ana sayfadaki en üst kısımdaki projelerim kısmındaki projeleri görüntülemeyi sağlayacak bu fonksiyon
    def tumProjeleriGoruntule(self) :
        self.cursor.execute('''
        SELECT
            projeID
            projeAdi,
            projeAciklama,
            baslangicTarihi,
            bitisTarihi
        FROM
            projeler
        WHERE
            1
        ''')
        self.conn.commit()

    def projedeToplamCalisanSayisi(self, projeID) :
        self.cursor.execute('''
        SELECT 
            projeID,
            COUNT(DISTINCT calisanID) AS calisanSayisi
        FROM 
            gorevler
        WHERE 
            projeID = ?;
        ''', (projeID,))








    """
    tablolariOlustur()
    #kullaniciEkle(ad = 'Hamzaaa', soyad = 'Bbbayar', mail = 'hamzabbbaya2333@gmail.com')
    #calisanEkle(kulID = 1, calAdi = 'firat', calSoyadi = 'evren', calMail= 'wwww22@gmail.com')

    kullaniciKisiselBilgilari(4)
    sonuc = self.cursor.fetchall()
    print (sonuc)

    calisanKisiselBilgilari()
    sonuc = self.cursor.fetchall()
    print (sonuc)

    self.conn.close()

    """