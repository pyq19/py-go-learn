package main
import "fmt"

type user struct {
    name string
    age byte
}

func (u user) Print() {
    fmt.Printf("%+v\n", u)
}

type Printer interface { // 接口类型
    Print()
}

func main() {
    var u user
    u.name = "Tom"
    u.age = 29
    var p Printer = u // 只要包含接口所需的全部方法，即表示实现了该接口
    p.Print()
}
// {name:Tom age:29}
