// 创建定制的日志记录器

package main
import (
    "io"
    "io/ioutil"
    "log"
    "os"
)

var (
    Trace   *log.Logger     // 记录所有日志
    Info    *log.Logger     // 重要的信息
    Warning *log.Logger     // 需要注意的信息
    Error   *log.Logger     // 非常严重的问题
)

func init() {
    file, err := os.OpenFile("errors.txt",
        os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0666)

    if err != nil {
        log.Fatalln("failed to open error log file:", err)
    }

    Trace = log.New(ioutil.Discard,
        "TRACE: ",
        log.Ldate|log.Ltime|log.Lshortfile)

    Info = log.New(os.Stdout,
        "INFO: ",
        log.Ldate|log.Ltime|log.Lshortfile)

    Warning = log.New(os.Stdout,
        "WARNING: ",
        log.Ldate|log.Ltime|log.Lshortfile)

    Error = log.New(io.MultiWriter(file, os.Stderr),
        "ERROR: ",
        log.Ldate|log.Ltime|log.Lshortfile)
}

func main() {
    Trace.Println("i have something standard to say")
    Info.Println("special information")
    Warning.Println("there is something you need to know about..")
    Error.Println("something has failed..")
}

// INFO: 2017/04/13 21:28:31 8-11.go:45: special information
// WARNING: 2017/04/13 21:28:31 8-11.go:46: there is something you need to know about..
// ERROR: 2017/04/13 21:28:31 8-11.go:47: something has failed..
// 还往errors.txt 写入了error信息
