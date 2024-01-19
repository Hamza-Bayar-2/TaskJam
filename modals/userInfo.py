class UserInfo :
    def __init__(
        self,
        userID,
        userName,
        userSurname,
        userMail,
        userPassword
            ) :
        self.userID = userID if(userID != None) else 0
        self.userName = userName
        self.userSurname = userSurname
        self.userMail = userMail
        self.userPassword = userPassword

    def __repr__(self):
        return f"SpendInfo(id={self.userID}, name='{self.userName}', surname={self.userSurname}, password={self.userPassword})"
