from sqlalchemy import create_engine,text

engine = create_engine(
    "mysql+pymysql://admin:1234admin@database-1.cxoago2k69og.eu-north-1.rds.amazonaws.com/projects?charset=utf8mb4")

def load_projects_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from myprojects"))
  myprojects=[]
  for row in result.all():
    myprojects.append(dict(row._mapping))
  return myprojects