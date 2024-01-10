import sqlite3 

# Veritabanına bağlanma
conn = sqlite3.connect('veritabani.db')
cursor = conn.cursor()

# görev durumu (tamamlanacak: 0, devam ediyor: 1, tamamlandi: 2 )
def tablolariOlustur() :
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS kullanicilar (  
      kullaniciID INTEGER PRIMARY KEY AUTOINCREMENT,  
      kullaniciAdi TEXT,  
      kullaniciSoyadi TEXT,    
      kullaniciMail TEXT,
      kullaniciSifre TEXT
    )T
  ''')
  cursor.execute('''
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
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS projeler (  
      projeID INTEGER PRIMARY KEY AUTOINCREMENT,  
      kullaniciID INTEGER,  
      projeAdi TEXT, 
      projeAciklama TEXT,
      baslangicTarihi DATE,  
      bitisTarihi DATE,
      gecikmeMiktari INTEGER,  
    )
  ''')
  cursor.execute('''
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
      gecikmeMiktari INTEGER,
    )
  ''')
  conn.commit()

def kullaniciEkle(ad, soyad, mail, sifre) :
  cursor.execute('''
    INSERT INTO kullanicilar(
      kullaniciAdi,
      kullaniciSoyadi,
      kullaniciMail,
      kullaniciSifre
    )
    VALUES(?, ?, ?, ?)
  ''', (ad, soyad, mail, sifre))
  conn.commit()
  
# kullanıcı kişisel bilgileri
def kullaniciKisiselBilgilari(kulID) :
  cursor.execute('''
    SELECT 
      kullaniciID,
      kullaniciAdi,
      kullaniciSoyadi,
      kullaniciMail
      kullaniciSifre          
    FROM
      kullanicilar
    WHERE
      kullaniciID = ?
  ''', (kulID,))
  conn.commit()
  
# isme soyada göre kullanıcı silme 
def kullaniciSil(ad, soyad) :
  cursor.execute('''
    DELETE
    FROM
      kullanicilar
    WHERE
      kullaniciAdi = ? AND kullaniciSoyadi = ?
  ''', (ad, soyad,))
  conn.commit()

# ID'ye göre kullanıcı silme 
def kullaniciSilID(kulID) :
  cursor.execute('''
    DELETE
    FROM
      kullanicilar
    WHERE
      kullaniciID = ?
  ''', (kulID,))
  conn.commit()











# çalışan eklerken ilk başta hiç bir görevi olmadığı için hepsine sıfır atıyoruz
def calisanEkle(kulID, calAdi, calSoyadi, calMail) :
  cursor.execute('''
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
  conn.commit()

# bütün çalışanları döndürür
def calisanKisiselBilgilari() :
  cursor.execute('''
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
  conn.commit()

# çalışana ait zamanında tamamlanan görevleri güncelleme
def calisanZamanindaTamamlananGuncelleme(zamaninda, calID, kulID) :
  cursor.execute('''
    UPDATE
      calisanlar
    SET
      zamanindaTamamlananGorevlerMiktari = ?
    WHERE
      calisanID = ? AND kullaniciID = ?
  ''', (zamaninda, calID, kulID,))
  conn.commit()

# çalışana ait zamanında tamamlanmayan görevleri güncelleme
def calisanZamanindaOlmayanGuncelleme(zamanindaOlmayan, calID, kulID) :
  cursor.execute('''
    UPDATE
      calisanlar
    SET
      zamanindaTamamlanamayanGorevlerMiktari = ?
    WHERE
      calisanID = ? AND kullaniciID = ?
  ''', (zamanindaOlmayan, calID, kulID,))
  conn.commit()

# isme soyada göre çalışan silem
def calisanSil(ad, soyad) :
  cursor.execute('''
    DELETE
    FROM
      calisanlar
    WHERE
      calisanAdi = ? AND calisanSoyadi = ?
  ''', (ad, soyad,))
  conn.commit()

# ID'ye göre çalışan silem
def calisanSilID(calID) :
  cursor.execute('''
    DELETE
    FROM
      calisanlar
    WHERE
      calisanID = ?
  ''', (calID,))
  conn.commit()











# proje eklerken ilk başta gecikme miktarını 0 ve zamanında tamamlandıyı true olarak atıyorum
def projeEkle(kulID, projeAdi, projeAciklama, basTarihi, bitTarihi) :
  cursor.execute('''
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
  conn.commit()

# projenin bilgilerini görüntülemek için bir fonksiyondur
def projeDetaySayfasi(projeID) :
  cursor.execute('''
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
  conn.commit()

# ana sayfadaki en üst kısımdaki projelerim kısmındaki projeleri görüntülemeyi sağlayacak bu fonksiyon
def tumProjeleriGoruntule() :
  cursor.execute('''
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
  conn.commit()

def projedeToplamCalisanSayisi(projeID) :
  cursor.execute('''
    SELECT 
      projeID,
      COUNT(DISTINCT calisanID) AS calisanSayisi
    FROM 
      gorevler
    WHERE 
      projeID = ?;
  ''', (projeID,))









tablolariOlustur()
#kullaniciEkle(ad = 'Hamzaaa', soyad = 'Bbbayar', mail = 'hamzabbbaya2333@gmail.com')
#calisanEkle(kulID = 1, calAdi = 'firat', calSoyadi = 'evren', calMail= 'wwww22@gmail.com')

kullaniciKisiselBilgilari(4)
sonuc = cursor.fetchall()
print (sonuc)

calisanKisiselBilgilari()
sonuc = cursor.fetchall()
print (sonuc)

conn.close()

