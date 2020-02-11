AGENT_MONITOR = {
    "ANSWER": {
        "TYPE": "MONITOR_UPDATE_VERSION_RESULT",
        "PAYLOAD": {
            "TYPE": {
                "UPDATE": "update",
                "ROLLBACK": "rollback"
            },
            "STATUS": {
                "SUCCESS": "success",
                "FAIL": "fail"
            }
        },
    },
    "REQUEST": {
        "TYPE": "MONITOR_UPDATE_VERSION",
    }
}
