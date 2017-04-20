// 使用最基本的log 包

package main

import "log"

func init() {
    log.SetPrefix("TRACE: ")
    log.SetFlags(log.Ldate | log.Lmicroseconds | log.Llongfile)
}

func main() {
    log.Println("message")      // Println 写到标准日志记录器

    log.Fatalln("fatal message")// Fatal 在调用Println() 之后会接着调用os.Exit(1)

    log.Panicln("panic message")// Panicln 在调用Println() 之后会接着调用panic()
}

// TRACE: 2017/04/13 21:15:08.946431 /Users/Mccree/p/py-go-learn/go/in-action/8-3.go:13: message
// TRACE: 2017/04/13 21:15:08.946505 /Users/Mccree/p/py-go-learn/go/in-action/8-3.go:15: fatal message
// exit status 1
