class TaskInfo :
    def __init__(
            self,
            taskID,
            projectId,
            workerId,
            taskTitle,
            startDate,
            finishDate,
            status,
            adam_gun_deger,
            lastTime,
            isCompletedTime
            ) -> None:
        
        self.taskId = taskId
        self.projectId = projectId
        self.workerId = workerId
        self.taskTitle = taskTitle
        self.startDate = startDate
        self.finishDate = finishDate
        self.status = status
        self.adam_gun_deger =adam_gun_deger
        self.lastTime = lastTime
        self.isCompletedTime = isCompletedTime

    def toMap(TaskInfo):
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
            "isCompletedTime" : TaskInfo.isCompletedTime
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
            Map["isCompletedTime"],
        )
