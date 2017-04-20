// method 重写，和匿名字段冲突一样的道理

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
    Human
    company string
}

// Human 定义method
func (h *Human) SayHi() {
    fmt.Printf("hi, i am [%s] you can call me on [%s]\n", h.name, h.phone)
}

// Employee 的method 重写Human 的method
func (e *Employee) SayHi() {
    fmt.Printf("hi, i'm <%s>, work at %s, call me on %s\n", e.name, e.company, e.phone)
}

func main() {
    mark := Student{Human{"MARK", 25, "122211111"}, "MIT COLLEDGE"}
    sam := Employee{Human{"SAM", 30, "123-123"}, "GOLANG INC"}

    mark.SayHi()
    sam.SayHi()
}
// hi, i am [MARK] you can call me on [122211111]
// hi, i'm <SAM>, work at GOLANG INC, call me on 123-123
