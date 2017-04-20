package main
import (
    "os"
    "log"
)

func main() {
    //f, err := os.Open(". /defer_.go")
    f, err := os.Open("/Users/Mccree/p/py-go-learn/go/go-note/defer/defer_.go")
    if err != nil {
        log.Fatalln(err)
    }
    defer f.Close()         // 仅注册，直到main退出前才执行

    println("do something////..")
}
// 2017/04/12 12:26:08 open . /defer_.go: no such file or directory
// exit status 1

// do something////..
