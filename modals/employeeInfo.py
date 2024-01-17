class EmployeeInfo :
    def __init__(
        self,
        employeeID,
        userID,
        employeeName,
        employeeSurname,
        employeeMail,
        AmountOfTasksCompletedOnTime,
        AmountOfTasksNotCompletedOnTime
            ) :
        self.employeeID = employeeID if(employeeID != None) else 0
        self.userID = userID
        self.employeeName = employeeName
        self.employeeSurname = employeeSurname
        self.employeeMail = employeeMail
        self.AmountOfTasksCompletedOnTime = AmountOfTasksCompletedOnTime if(AmountOfTasksCompletedOnTime != None) else 0
        self.AmountOfTasksNotCompletedOnTime = AmountOfTasksNotCompletedOnTime if(AmountOfTasksNotCompletedOnTime != None) else 0
    def __repr__(self):
        return f"EmployeeInfo(id={self.employeeID})"
