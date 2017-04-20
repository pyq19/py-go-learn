// method 继承，如果匿名字段实现了一个method，
// 那么包含这个匿名字段的struct 也能调用该method

package main
import "fmt"

type Human struct {
    name string
    age int
    phone string
}

type Student struct {
    Human               // 匿名字段
    school string
}

type Employee struct {
    Human               // 匿名字段
    company string
}

// 在human 上面定义了一个method
func (h *Human) SayHi() {
    fmt.Printf("hi i am [%s] you can call me on [%s]\n", h.name, h.phone)
}

func main() {
    mark := Student{Human{"marlk", 20, "1123-1233111"}, "youqu"}
    sam := Employee{Human{"Sam", 30, "123-1111-222-22"}, "golang Inc."}

    mark.SayHi()
    sam.SayHi()
}
// hi i am [marlk] you can call me on [1123-1233111]
// hi i am [Sam] you can call me on [123-1111-222-22]
