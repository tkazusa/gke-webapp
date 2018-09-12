# mycroservicized ML web application 
## Example 
### Add users to docker group
```bash
$ sudo gpasswd -a [username] docker
```

### Build both frontend and  backend images and run containers with them.
```bash
$ make build
$ make run
```
### Stop containers and remove images
```bash
$ make clean
```
From your local browser, accsess `http://localhost:8080`.
