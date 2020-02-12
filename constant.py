AGENT_MONITOR = {
    "TYPE": {
        "REQUEST": "MONITOR_UPDATE_VERSION",
        "ANSWER": "MONITOR_UPDATE_VERSION_RESULT",
    },
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
}
