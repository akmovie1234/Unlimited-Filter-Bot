From flask import  flask
app =flask(__name__)

@app.router('/')
defhello_world():
  return 'greyMatters'


if__name__=='__main__':
 app.run()
