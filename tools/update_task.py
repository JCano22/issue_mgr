import requests

BACKEND_URL = "http://127.0.0.1:5000/tasks/"

def update_task(summary, description, is_active, pk):
    url = "%s%s" % (BACKEND_URL, pk)
    updated_task_data= {
        "summary": summary,
        "description": description
    }
    response = requests.put(BACKEND_URL, json=updated_task_data)
    if response.status_code == 204:
        print("Task updated succesfully")
    else:
        print("Something went wrong while updating task")



