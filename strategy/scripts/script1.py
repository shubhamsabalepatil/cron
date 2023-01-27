import schedule

def first_script():
  print("First Script")

schedule.every(2).seconds.do(first_script)

while True:
  schedule.run_pending()