from flask import Flask,jsonify,request

app = Flask(__name__) 


tasks = [
    {
    'id': 1,
    'contact': '998744456',
    'name': 'Raju',
    'done': False
    },

    {
    id': 2,
    'contact': '998754456',
    'name': 'rahul',
    'done': False
    },
 ]

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "please provide data"
        }, 400)

    else:
        task = {
            "id": tasks[-1]['id']+1,
            "name": request.json['name'],
            "contact": request.json.get['contact'],
            "done": False
        }

        tasks.append(task)
        return jsonify({
            "status": "success",
            "message": "task added success"
        })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    }) 


if __name__ == "__main__":
    app.run()
