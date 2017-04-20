// 使用io.Reader 和io.Writer 接口写一个简单版本的curl

package main
import (
    "io"
    "log"
    "net/http"
    "os"
)

func main() {
    r, err := http.Get(os.Args[1])      // r 是一个响应，r.Body 是io.Reader
    if err != nil {
        log.Fatalln(err)
    }

    file, err := os.Create(os.Args[2])
    if err != nil {
        log.Fatalln(err)
    }
    defer file.Close()

    dest := io.MultiWriter(os.Stdout, file) // 使用MultiWriter 就可以同时向文件和标准输出设备进行写操作

    io.Copy(dest, r.Body)   // 读出响应的内容，并写到两个目的地
    if err := r.Body.Close(); err != nil {
        log.Println(err)
    }
}
// go run 8-46.go http://localhost:8000 test.txt
