from flask_migrate import Migrate, MigrateCommand

from flask_script import Manager,Server


from app import app,db
migrate = Migrate(app,db)





if __name__ == '__main__':
    app.run(debug=True)
    
