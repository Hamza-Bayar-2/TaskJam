class SelectedEmployee :
    def __init__(
        self,
        employeeName,
        employeeSurname,
        employeeMail,
        AmountOfTasksCompletedOnTime,
        AmountOfTasksNotCompletedOnTime,
        goingToCompleteTasks,
        ongoingTasks,
        completedTasks
    ) : 
        self.employeeName = employeeName
        self.employeeSurname = employeeSurname
        self.employeeMail = employeeMail
        self.AmountOfTasksCompletedOnTime = AmountOfTasksCompletedOnTime
        self.AmountOfTasksNotCompletedOnTime = AmountOfTasksNotCompletedOnTime
        self.goingToCompleteTasks = goingToCompleteTasks
        self.ongoingTasks = ongoingTasks
        self.completedTasks = completedTasks