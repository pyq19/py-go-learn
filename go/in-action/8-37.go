// 不用标准库的不同函数
// 使用io.Writer 接口

package main
import (
    "bytes"
    "fmt"
    "os"
)

func main() {
    var b bytes.Buffer      // 创建一个Buffer 值，并将一个字符串写入Buffer，使用实现io.Writer 的Write 方法
    b.Write([]byte("hello "))

    fmt.Fprintf(&b, "world")// 使用Fprintf将一个字符串拼接到Buffer 里，将bytes.Buffer 的地址作为io.Writer 类型值传入

    b.WriteTo(os.Stdout)    // 将Buffer 的内容输出到标准输出设备，将os.File 值的地址作为io.Writer 类型值传入
}
// hello world%
