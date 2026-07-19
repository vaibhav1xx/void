def execute(tasks):

    execution = []

    for task in tasks:

        execution.append(
            {
                "action": task.action,
                "target": task.target,
                "status": task.status
            }
        )

    return execution