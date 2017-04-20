// 使用io.Reader / io.Writer接口写简单版本curl程序
package main
import (
    "fmt"
    "io"
    "net/http"
    "os"
)

// init 在main 函数之前调用
func init() {
    if len(os.Args) != 2 {
        fmt.Println("Usage -> ./example2 <url>")
        os.Exit(-1)
    }
}

func main() {
    // 从web 服务器得到响应
    r, err := http.Get(os.Args[1])
    if err != nil {
        fmt.Println(err)
        return
    }

    // 从Body 复制到stdout
    io.Copy(os.Stdout, r.Body)
    if err := r.Body.Close(); err != nil {
        fmt.Println(err)
    }
}
// Usage -> ./example2 <url>
// exit status 255
