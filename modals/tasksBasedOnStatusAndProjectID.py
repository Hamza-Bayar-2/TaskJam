class TasksBasedOnStatusAndProjectID :
    def __init__(
        self,
        taskID,
        taskName,
        taskDescription,
        startingDate,
        endDate,
        delayAmount
    ) :
        self.taskID = taskID
        self.taskName = taskName
        self.taskDescription = taskDescription
        self.startingDate = startingDate
        self.endDate = endDate
        self.delayAmount = delayAmount