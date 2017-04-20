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

// 打印
func (p Person) String() string {
    return "name ->" + p.name + "age ->" + strconv.Itoa(p.age)
}

func main() {
    list := make(List, 3)
    list[0] = 1                 // an int
    list[1] = "hello"           // an string
    list[2] = Person{"MCC", 25}

    for index, element := range list {
        switch value := element.(type) {
            case int:
                fmt.Printf("list[%d] is an int, value ->%d\n", index, value)
            case string:
                fmt.Printf("list[%d] is a string, value ->%s\n", index, value)
            case Person:
                fmt.Printf("list[%d] is a Person, value ->%s\n", index, value)
            default:
                fmt.Println("list[%d] is of a different type", index)
        }
    }
}
// list[0] is an int, value ->1
// list[1] is a string, value ->hello
// list[2] is a Person, value ->name ->MCCage ->25
