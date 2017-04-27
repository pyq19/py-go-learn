package main

/*
import "github.com/jinzhu/gorm"
import _ "github.com/go-sql-driver/mysql"   // 导入数据库驱动
// import _ "github.com/jinzhu/gorm/dialects/postgres"
// import _ "github.com/jinzhu/gorm/dialects/sqlite"
// import _ "github.com/jinzhu/gorm/dialects/mssql"

func main() {
    db, err := gorm.Open("mysql", "root:forever@/test?charset=utf8&parseTime=Ture&loc=Local")
    if err != nil {
        print(err)
        print("go err??")
    }
    defer db.Close()
}
// (0x13ee9a0,0xc420152830)go err??%
*/

// sqlite3
import (
    "github.com/jinzhu/gorm"
    _ "github.com/jinzhu/gorm/dialects/sqlite"
)

func main() {
    db, err := gorm.Open("sqlite3", "test.db")
    if err != nil {
        panic("failed to connect database")
    }
    defer db.Close()
}
