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
            "FAIL": "fail",
            "PROGRESS": "progress"
        },
        "CONTAINERTYPE": {
            "BACKEND": "docker_918f055b-ee97-4f4a-a4f1-e516d8812262",
            "RABBITMQ": "docker_adacf0fa-7941-4655-ad9d-91859602aba9",
            "DATABASE": "docker_df01f315-bfed-4750-963f-5c30e9a19d2f",
            "MONITOR": "docker_f9a80799-e456-482b-9896-0265cb49b242"
        }
    },
}
