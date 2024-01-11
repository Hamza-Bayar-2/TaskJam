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
            CREATE TABLE IF NOT EXISTS users (  
                userID INTEGER PRIMARY KEY AUTOINCREMENT,  
                userName TEXT,  
                userSurname TEXT,    
                userMail TEXT,
                userPassword TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (  
                employeeID INTEGER PRIMARY KEY AUTOINCREMENT,  
                userID INTEGER,  
                employeeName TEXT,  
                employeeSurname TEXT,  
                employeeMail TEXT,   
                AmountOfTasksCompletedOnTime INTEGER,   
                AmountOfTasksNotCompletedOnTime INTEGER
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS projects (  
                projectID INTEGER PRIMARY KEY AUTOINCREMENT,  
                userID INTEGER,  
                projectName TEXT, 
                projectDescription TEXT,
                startingDate DATE,  
                endDate DATE,
                delayAmount INTEGER
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (  
                taskID INTEGER PRIMARY KEY AUTOINCREMENT,  
                projectID INTEGER,  
                employeeID INTEGER,
                taskName TEXT,
                taskDescription TEXT,
                startingDate DATE,
                endDate DATE,
                taskStatus INTEGER,                   
                delayAmount INTEGER
            )
        ''')
        self.conn.commit()

    def kullaniciEkle(self, UserInfo) :
        self.cursor.execute('''
            INSERT INTO users(
                userName,
                userSurname,
                userMail,
                userPassword
            )
            VALUES(?, ?, ?, ?)
        ''', (UserInfo.userName, UserInfo.userSurname, UserInfo.userMail, UserInfo.userPassword))
        self.conn.commit()
        
    # kullanıcı kişisel bilgileri
    def kullaniciKisiselBilgilari(self, userMail) :
        self.cursor.execute('''
            SELECT 
                userID,
                userName,
                userSurname,
                userMail,
                userPassword          
            FROM
                users
            WHERE
                userMail = ?
        ''', (userMail,))
        self.conn.commit()
        userList = self.cursor.fetchall()
        return userList 
        
    # isme soyada göre kullanıcı silme 
    def kullaniciSil(self, userName, userSurname) :
        self.cursor.execute('''
            DELETE
            FROM
                users
            WHERE
                userName = ? AND userSurname = ?
        ''', (userName, userSurname,))
        self.conn.commit()

    # ID'ye göre kullanıcı silme 
    def kullaniciSilID(self, userID) :
        self.cursor.execute('''
            DELETE
            FROM
                users
            WHERE
                userID = ?
        ''', (userID,))
        self.conn.commit()











    # çalışan eklerken ilk başta hiç bir görevi olmadığı için hepsine sıfır atıyoruz
    def calisanEkle(self, userID, employeeName, employeeSurname, employeeMail) :
        self.cursor.execute('''
            INSERT INTO employees(
                userID,
                employeeName,
                employeeSurname,
                employeeMail,
                AmountOfTasksCompletedOnTime,
                AmountOfTasksNotCompletedOnTime
            )
            VALUES(?, ?, ?, ?, ?, ?)
        ''', (userID, employeeName, employeeSurname, employeeMail, 0, 0,))
        self.conn.commit()

    # bütün çalışanları döndürür
    def calisanKisiselBilgilari(self) :
        self.cursor.execute('''
            SELECT
                employeeID,
                userID,
                employeeName,
                employeeSurname,
                employeeMail,
                AmountOfTasksCompletedOnTime,
                AmountOfTasksNotCompletedOnTime
            FROM
                employees
            WHERE
                1
        ''')
        self.conn.commit()

    # çalışana ait zamanında tamamlanan görevleri güncelleme
    def calisanZamanindaTamamlananGuncelleme(self, onTime, employeeID, userID) :
        self.cursor.execute('''
            UPDATE
                employees
            SET
                AmountOfTasksCompletedOnTime = ?
            WHERE
                employeeID = ? AND userID = ?
        ''', (onTime, employeeID, userID,))
        self.conn.commit()

    # çalışana ait zamanında tamamlanmayan görevleri güncelleme
    def calisanZamanindaOlmayanGuncelleme(self, notOnTime, employeeID, userID) :
        self.cursor.execute('''
            UPDATE
                employees
            SET
                AmountOfTasksNotCompletedOnTime = ?
            WHERE
            employeeID = ? AND userID = ?
        ''', (notOnTime, employeeID, userID,))
        self.conn.commit()

    # isme soyada göre çalışan silem
    def calisanSil(self, employeeName, employeeSurname) :
        self.cursor.execute('''
            DELETE
            FROM
                employees
            WHERE
                employeeName = ? AND employeeSurname = ?
        ''', (employeeName, employeeSurname,))
        self.conn.commit()

    # ID'ye göre çalışan silem
    def calisanSilID(self, employeeID) :
      self.cursor.execute('''
        DELETE
        FROM
            employees
        WHERE
            employeeID = ?
      ''', (employeeID,))
      self.conn.commit()











    # proje eklerken ilk başta gecikme miktarını 0 ve zamanında tamamlandıyı true olarak atıyorum
    def projeEkle(self, kulID, projectName, projectDescription, startingDate, endDate) :
        self.cursor.execute('''
            INSERT INTO projects(
                userID,
                projectName,
                projectDescription,
                startingDate,
                endDate,
                delayAmount,
            )
            VALUES(?, ?, ?, ?, ?, ?)
        ''', (kulID, projectName, projectDescription, startingDate, endDate, 0,))
        self.conn.commit()

    # projenin bilgilerini görüntülemek için bir fonksiyondur
    def projeDetaySayfasi(self, projectID) :
        self.cursor.execute('''
            SELECT
                projectName,
                projectDescription,
                startingDate,
                endDate,
                delayAmount
            FROM
                projects
            WHERE
                projectID = ?
        ''', (projectID,))
        self.conn.commit()

    # ana sayfadaki en üst kısımdaki projectsim kısmındaki projectsi görüntülemeyi sağlayacak bu fonksiyon
    def tumprojectsiGoruntule(self) :
        self.cursor.execute('''
            SELECT
                projectID
                projectName,
                projectDescription,
                startingDate,
                endDate
            FROM
                projects
            WHERE
                1
        ''')
        self.conn.commit()

    def projedeToplamCalisanSayisi(self, projectID) :
        self.cursor.execute('''
            SELECT 
                projectID,
                COUNT(DISTINCT employeeID) AS calisanSayisi
            FROM 
                tasks
            WHERE 
                projectID = ?;
        ''', (projectID,))








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