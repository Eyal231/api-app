1. **git clone git@github.com:Eyal231/api-app.git**

2. **source runall**
3. ****test cluster:****
   **chack services:**
   >kubectl get services
   >kubectl get pods
   >kubectl get ingress # wait for the ingress get his ip address

****testing:****
- curl 192.168.58.2/
  > "welcome to the book api" server XXX
- curl 192.168.58.2/book/1984
  > [{"book":"1984","genre":"Dystopian","author":"George Orwell"},{"server":"Book API Server","version":"1.0","status":"Running"}]
- curl 192.168.58.2/author/eyal
  > [{"name":"eyal","books":["Harry Potter and the Sorcerer Stone"]},{"server":"author API Server","version":"1.0","status":"Running"}]

