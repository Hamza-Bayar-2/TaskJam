import sqlite3 

# Veritabanına bağlanma
conn = sqlite3.connect('veritabani.db')
cursor = conn.cursor()

# görev durumu (tamamlanacak: 0, tamamlandi: 1, devam ediyor: 2)
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
      basliyacagiGorevlerMiktari INTEGER,  
      tamamlananGorevlerMiktari INTEGER,  
      devamEdenGorevlerMiktari INTEGER,  
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
      zamanindaTamamlandi BOOLEAN
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
      durum INTEGER,                   
      adamGunDegeri INTEGER,
      gecikmeMiktari INTEGER,
      zamanindaTamamlandi BOOLEAN
    )
  ''')
  conn.commit()

def kullaniciEkle(ad, soyad, mail) :
  cursor.execute('''
    INSERT INTO kullanicilar(
      kullaniciAdi,
      kullaniciSoyadi,
      kullaniciMail
    )
    VALUES(?, ?, ?)''', (ad, soyad, mail,))
  conn.commit()
  
# kullanıcı kişisel bilgileri
def kullaniciKisiselBilgilari(kulID) :
  cursor.execute('''
    SELECT 
      kullaniciID,
      kullaniciAdi,
      kullaniciSoyadi,
      kullaniciMail
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
    basliyacagiGorevlerMiktari,
    tamamlananGorevlerMiktari,
    devamEdenGorevlerMiktari,
    zamanindaTamamlananGorevlerMiktari,
    zamanindaTamamlanamayanGorevlerMiktari
    )
    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
  ''', (kulID, calAdi, calSoyadi, calMail, 0, 0, 0, 0, 0,))

# bütün çalışanları döndürür
def calisanKisiselBilgilari() :
  cursor.execute('''
    SELECT
      calisanID,
      kullaniciID,
      calisanAdi,
      calisanSoyadi,
      calisanMail,
      basliyacagiGorevlerMiktari,
      tamamlananGorevlerMiktari,
      devamEdenGorevlerMiktari,
      zamanindaTamamlananGorevlerMiktari,
      zamanindaTamamlanamayanGorevlerMiktari
    FROM
      calisanlar
    WHERE
      1
  ''')
  conn.commit()

# çalışanın ististanıs tüm görevleri
# görevler tablosu ile inner join yapmalı.
def calisanaAitTumGorevler() :
  cursor.execute('''
    
  ''')

# çalışana ait başlayacağı görevleri güncelleme
def calisanBaslayacagiGorevGuncelleme(basliyacagi, calID, kulID) :
  cursor.execute('''
    UPDATE
      calisanlar
    SET
      basliyacagiGorevlerMiktari = ?
    WHERE
      calisanID = ? AND kullaniciID = ?
  ''', (basliyacagi, calID, kulID,))
  conn.commit()

# çalışana ait tamamlanan görevleri güncelleme
def calisantamamlananGorevGuncelleme(tamamlanan, calID, kulID) :
  cursor.execute('''
    UPDATE
      calisanlar
    SET
      tamamlananGorevlerMiktari = ?
    WHERE
      calisanID = ? AND kullaniciID = ?
  ''', (tamamlanan, calID, kulID,))
  conn.commit()

# çalışana ait devam eden görevleri güncelleme
def calisanDevamEdenGorevGuncelleme(devamEden, calID, kulID,) :
  cursor.execute('''
    UPDATE
      calisanlar
    SET
      devamEdenGorevlerMiktari = ?
    WHERE
      calisanID = ? AND kullaniciID = ?
  ''', (devamEden, calID, kulID,))
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

