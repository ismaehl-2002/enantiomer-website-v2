from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://zi6id5p25yfq60ih6t1y:pscale_pw_OG991jS2It86MJJqrCYvCmcJ5psfFaYkxyOLA9GoTwy@ap-south.connect.psdb.cloud/enantiomer?charset=utf8mb4" 

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
  jobs = []
  for row in result.all():
    jobs.append(row)
    return jobs