from __init__ import create_app

#run the app in this file

app=create_app()

if __name__=="__main__":
    app.run(debug=True,port=5000)