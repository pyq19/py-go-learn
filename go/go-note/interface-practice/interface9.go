// interface 函数参数

package main
import (
    "fmt"
    "strconv"
)

type Human struct {
    name string
    age int
    phone string
}

func (h Human) String() string {
    return " " + h.name + " - " + strconv.Itoa(h.age) + " years, phone -> " + h.phone
}

func main() {
    Bob := Human{"Bob", 39, "123-456"}
    fmt.Println("this human is ->", Bob)
}
// this human is ->  Bob - 39 years, phone -> 123-456
