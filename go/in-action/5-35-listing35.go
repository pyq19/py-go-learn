// 展示bytes.Buffer 也可用于io.Copy 函数

package main
import (
    "bytes"
    "fmt"
    "io"
    "os"
)

func main() {
    var b bytes.Buffer

    // 将字符串写入Buffer
    b.Write([]byte("hello..."))

    // 使用Fprintf 将字符串拼接到Buffer
    fmt.Fprintf(&b, "world...")

    // 将Buffer 的内容写到Stdout
    io.Copy(os.Stdout, &b)
}
// hello...world...%
