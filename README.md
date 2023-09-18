git clone git@github.com:Eyal231/api-app.git

source runall

testing:
- curl 192.168.58.2/
  > "welcome to my book api" server XXX
- curl 192.168.58.2/book/1984
  

- curl 192.168.58.2/author/eyal
  > harry poter
  >

