package main
import "fmt"

func main() {
    type (                  // 组
        user struct {       // 结构体
            name string
            age uint8
        }

        event func (string) bool // 函数类型
    )

    u := user{"Tom", 20}
    fmt.Println(u)

    var f event = func (s string) bool {
        println(s)
        return s!= ""
    }

    f("abc")
}
// {Tom 20}
// abc
