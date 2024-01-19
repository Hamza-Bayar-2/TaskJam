class TaskInfo :
    def __init__(
            self,
            taskID, #INT
            projectID, #INT
            employeeID, #INT
            taskName, #TEXT
            taskDescription, #TEXT
            startingDate, #TEXT
            endDate, #TEXT
            taskStatus, #INT
            delayAmount, #INT
            ) -> None:
        
        self.taskID = taskID
        self.projectID = projectID
        self.employeeID = employeeID
        self.taskName = taskName
        self.taskDescription = taskDescription
        self.startingDate = startingDate
        self.endDate = endDate
        self.taskStatus = taskStatus
        self.delayAmount = delayAmount
    
    def __repr__(self):
        return f"TaskInfo(id={self.projectID}, employeeID='{self.employeeID}', taskName={self.taskName})"

"""def toMap(TaskInfo):
    return {
        "taskId" : TaskInfo.taskId,
        "projectId" : TaskInfo.projectId,
        "workerId" : TaskInfo.workerId,
        "taskTitle" : TaskInfo.taskTitle,
        "startDate" : TaskInfo.startDate,
        "finishDate" : TaskInfo.finishDate,
        "status" : TaskInfo.status,
        "adam_gun_deger" : TaskInfo.adam_gun_deger,
        "lastTime" : TaskInfo.lastTime,
    }
def fromMap(Map):
    return TaskInfo(
        Map["taskId"],
        Map["projectId"],
        Map["workerId"],
        Map["taskTitle"],
        Map["startDate"],
        Map["finishDate"],
        Map["status"],
        Map["adam_gun_deger"],
        Map["lastTime"],
    )
"""