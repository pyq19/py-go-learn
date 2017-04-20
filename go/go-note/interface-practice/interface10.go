// interface 变量存储的类型

package main
import (
    "fmt"
    "strconv"
)

type Element interface{}
type List []Element

type Person struct {
    name string
    age int
}

// 定义String 方法，实现了fmt.Stringer
func (p Person) String() string {
    return "name ->" + p.name + "age ->" + strconv.Itoa(p.age)
}

func main() {
    list := make(List, 3)
    list[0] = 1             // an int
    list[1] = "hello"
    list[2] = Person{"TOM", 18}

    for index, element := range list {
        if value, ok := element.(int); ok {
            fmt.Printf("list[%d] is an int and its value is %d\n", index, value)
        } else if value, ok := element.(string); ok {
            fmt.Printf("list[%d] is an string and its value is %s\n", index, value)
        } else if value, ok := element.(Person); ok {
            fmt.Printf("list[%d] is a Person and its value is %s\n", index, value)
        } else {
            fmt.Printf("list[%d] is of a different type", index)
        }
    }
}
// List[0] is an int and its value is 1
// List[1] is an string and its value is hello
// List[2] is a Person and its value is name ->TOMage ->18
