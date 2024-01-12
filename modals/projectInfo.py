class ProjectInfo :
    def __init__(
        self,
        projectID,
        projectName,
        projectDescription,
        startingDate,
        endDate,
        delayAmount,
            ) :
        self.projectID = projectID if(projectID != None) else 0
        self.projectName = projectName
        self.projectDescription = projectDescription
        self.startingDate = startingDate
        self.endDate = endDate
        self.delayAmount = delayAmount

    def __repr__(self):
        return f"SpendInfo(id={self.projectID}, name='{self.projectName}', projectDescription={self.projectDescription})"
