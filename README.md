# MySQL Docker

## 起動
```
$ docker-compose up -d
```

## root接続
```
$ docker exec -it mysql_server bash
$ mysql -u root -padmin
```

## user接続
```
$ mysql -u user -h {host名} -ppassword
```
