import sqlite3 
from modals.userInfo import UserInfo
from modals.projectInfo import ProjectInfo

class db_Helper:
    def __init__(self) -> None:
    # Veritabanına bağlanma
        self.conn = sqlite3.connect('veritabani.db')
        self.cursor = self.conn.cursor()
        self.createTables()

    # task status (tamamlanacak: 0, devam ediyor: 1, tamamlandi: 2 )
    def createTables(self) :
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
                startingDate TEXT,  
                endDate TEXT,
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
                startingDate TEXT,
                endDate TEXT,
                taskStatus INTEGER,                   
                delayAmount INTEGER
            )
        ''')
        self.conn.commit()

    def addNewUser(self, UserInfo) :
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
    def showUserInformation(self, userMail) :
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
        return UserInfo(
            userID = userList[0][0],
            userName= userList[0][1], 
            userSurname= userList[0][2], 
            userMail= userList[0][3], 
            userPassword= userList[0][4]
        ) if len(userList) > 0 else None
        
    # isme soyada göre kullanıcı silme 
    def deleteUser(self, userMail) :
        self.cursor.execute('''
            DELETE
            FROM
                users
            WHERE
                userMail = ?
        ''', (userMail,))
        self.conn.commit()

    # ID'ye göre kullanıcı silme 
    def deleteUserID(self, userID) :
        self.cursor.execute('''
            DELETE
            FROM
                users
            WHERE
                userID = ?
        ''', (userID,))
        self.conn.commit()











    # çalışan eklerken ilk başta hiç bir görevi olmadığı için hepsine sıfır atıyoruz
    def addNewEmployee(self, userID, employeeName, employeeSurname, employeeMail) :
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
    def showEmployeeInformation(self) :
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
    def employeeAmountOfTasksCompletedOnTimeUpdate(self, onTime, employeeID, userID) :
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
    def employeeAmountOfTasksCompletedNotOnTimeUpdate(self, notOnTime, employeeID, userID) :
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
    def deleteEmployee(self, employeeName, employeeSurname) :
        self.cursor.execute('''
            DELETE
            FROM
                employees
            WHERE
                employeeName = ? AND employeeSurname = ?
        ''', (employeeName, employeeSurname,))
        self.conn.commit()

    # ID'ye göre çalışan silem
    def deleteEmployeeID(self, employeeID) :
      self.cursor.execute('''
        DELETE
        FROM
            employees
        WHERE
            employeeID = ?
      ''', (employeeID,))
      self.conn.commit()











    # proje eklerken ilk başta gecikme miktarını 0 ve zamanında tamamlandıyı true olarak atıyorum
    def addNewProject(self, UserInfo, ProjectInfo) :
        self.cursor.execute('''
            INSERT INTO projects(
                userID,
                projectName,
                projectDescription,
                startingDate,
                endDate,
                delayAmount
            )
            VALUES(?, ?, ?, ?, ?, ?)
        ''', (UserInfo.userID, ProjectInfo.projectName, ProjectInfo.projectDescription, ProjectInfo.startingDate, ProjectInfo.endDate, 0))
        self.conn.commit()
        print(self.cursor.fetchall())

    # projenin detaylarını detaylar sayfasında görüntülemek için kullanılır
    def showProjectOnDetailPage(self, projectID) :
    # projenin bilgilerini görüntülemek için bir fonksiyondur
    def projectDetailPage(self, projectName) :
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
                projectName = ?
        ''', (projectID,))
        self.conn.commit()
        project = self.cursor.fetchall()
        return ProjectInfo(projectID= project[0][0], projectName = project[0][1], projectDescription = project[0][2], startingDate = project[0][3], endDate = project[0][4], delayAmount= project[0][4]) if len(project) !=0 else None

    # ana sayfadaki en üst kısımdaki projectsim kısmındaki projectsi görüntülemeyi sağlayacak bu fonksiyon
    def showAllProjects(self, userId) :
        self.cursor.execute('''
            SELECT
                projectID,
                projectName,
                projectDescription,
                startingDate,
                endDate,
                delayAmount  
            FROM
                projects
            WHERE
                userID = ?
        ''', (userId,))
        self.conn.commit()
        projectsList = []
        for item in self.cursor.fetchall() :
            projectsList.append(
                ProjectInfo(
                    projectID= item[0],
                    projectName = item[1],
                    projectDescription = item[2],
                    startingDate = item[3], 
                    endDate = item[4], 
                    delayAmount= item[4]
                )
            )
        return projectsList

    def showTotalNumberOfEmployeesInTheProject(self, projectID) :
        self.cursor.execute('''
            SELECT 
                projectID,
                COUNT(DISTINCT employeeID) AS calisanSayisi
            FROM 
                tasks
            WHERE 
                projectID = ?
        ''', (projectID,))

    # bu fonksiyon projenin gecikme miktarını en geç tamamlanan göreve göre setlemektedir
    def updateProjectDelayAmount(self, projectID) :
        self.cursor.execute('''
            UPDATE 
                projects
            SET 
                delayAmount = (
                    SELECT 
                        MAX(delayAmount)
                    FROM 
                        tasks
                    WHERE 
                        tasks.projectID = projects.projectID
                )
            WHERE projectID = ?;
        ''', (projectID,))

    def updateProject(self, projectName, projectDescription, startingDate, endDate, projectID) :
        self.cursor.execute('''
            UPDATE projects
            SET 
                projectName = ?,
                projectDescription = ?,
                startingDate = ?,
                endDate = ?
            WHERE 
                projectID = ?
        ''', (projectName, projectDescription, startingDate, endDate, projectID,))

    def deleteProject(self, projectID) :
        self.cursor.execute('''
            DELETE FROM 
                projects
            WHERE 
                projectID = ?
        ''', (projectID,))











    # taskStatus yani görev durumu tamamlanacak: 0 olarak atıyoruz. 
    def addNewTask(self, projectID, employeeID, taskName, taskDescription, startingDate, endDate) :
        self.cursor.execute('''
            INSERT INTO projects(
                projectID = ?,
                employeeID = ?,
                taskName = ?,
                taskDescription = ?,
                startingDate = ?,
                endDate = ?,
                taskStatus = ?,
                delayAmount = ?
            )
            VALUES(?, ?, ?, ?, ?, ?, ?, ?)
        ''', (projectID, employeeID, taskName, taskDescription, startingDate, endDate, 0, 0,))

    def updateTask(self, employeeID, taskName, taskDescription, startingDate, endDate, taskID) :
        self.cursor.execute('''
            UPDATE 
                tasks
            SET 
                employeeID = ?,
                taskName = ?,
                taskDescription = ?,
                startingDate = ?,
                endDate = ?,
            WHERE 
                taskID = ?
        ''', (employeeID, taskName, taskDescription, startingDate, endDate, taskID,))

    # gorev durumunu guncellemek icindir (tamamlanacak: 0, devam ediyor: 1, tamamlandi: 2 )
    def updateTaskStatus(self, taskStatus, taskID) :
        self.cursor.execute('''
            UPDATE 
                tasks
            SET 
                taskStatus = ?,
            WHERE 
                taskID = ?
        ''', (taskStatus, taskID))

    # görevin gecikme miktarını güncellemeye yarar
    def updateTaskDelayAmount(self, delayAmount, taskID) :
        self.cursor.execute('''
            UPDATE 
                tasks
            SET 
                delayAmount = ?,
            WHERE 
                taskID = ?
        ''', (delayAmount, taskID))

    # görevin detaylarını görev detayları sayfasında görüntülemeyi yarar
    def showTaskOnDetailPage(self, taskID) :
        self.cursor.execute('''
            SELECT 
                employeeID,
                taskName,
                taskDescription,
                startingDate,
                endDate,
                taskStatus,
                delayAmount
            FROM 
                tasks
            WHERE
                taskID = ?
        ''', (taskID,))

    # !!!!!!!!!!!!! burası bitmedi daha kullanıcı adını alacam



    """
    createTables()
    #addNewUser(ad = 'Hamzaaa', soyad = 'Bbbayar', mail = 'hamzabbbaya2333@gmail.com')
    #addEmployee(kulID = 1, calAdi = 'firat', calSoyadi = 'evren', calMail= 'wwww22@gmail.com')

    userInformation(4)
    sonuc = self.cursor.fetchall()
    print (sonuc)

    employeeInformation()
    sonuc = self.cursor.fetchall()
    print (sonuc)

    self.conn.close()

    """