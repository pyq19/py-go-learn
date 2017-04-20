package main
import "fmt"

type Human struct {
    name string
    age int
    phone string
}

type Student struct {
    Human
    school string
    loan float32
}

type Employee struct {
    Human
    company string
    money float32
}

// Human 实现SayHi 方法
func (h Human) SayHi() {
    fmt.Printf("hi i am %s you can call me on %s\n", h.name, h.phone)
}

// Human 实现Sing 方法
func (h Human) Sing(lyrics string) {
    fmt.Println("lalalalala ->", lyrics)
}

// Employee 重载Human 的SayHi 方法
func (e Employee) SayHi() {
    fmt.Printf("hi i am %s, i work at %s. call me on %s\n", e.name, e.company, e.phone)
}

// Interface Men 被Human，Student 和Employee 实现
// 因为这三个类型都实现了这两个方法
type Men interface {
    SayHi()
    Sing(lyrics string)
}

func main() {
    mike := Student{Human{"MIKE", 25, "123-123"}, "Mit", 0.0000}
    paul := Student{Human{"PAUL", 26, "12345-89"}, "Harvard", 100.0}
    sam := Employee{Human{"SAM", 30, "12-34-56"}, "GOLANG INC", 200.00}
    Tom := Employee{Human{"TOM", 45, "2345-67"}, "BMW INC", 300.00}

    var i Men       // Men 类型的变量 i

    i = mike        // i 能存储student
    // fmt.Println("this is <%s>, a student ....", i.name) // ERROR !
    fmt.Println("this is mike, a student.. ->")
    i.SayHi()
    i.Sing(" mike hihihihihi song")

    i = Tom
    fmt.Println("this is tom, an employee ->")
    i.SayHi()
    i.Sing("tom's song...lalala")

    x := make([]Men, 3)     // 定义了slice Men
    x[0], x[1], x[2] = paul, sam, mike  // 这三个都是不同类型的元素，但是都实现了interface 同一个接口

    for _, value := range x {
        value.SayHi()
    }
}
// this is mike, a student.. ->
// hi i am MIKE you can call me on 123-123
// lalalalala ->  mike hihihihihi song
// this is tom, an employee ->
// hi i am TOM, i work at BMW INC. call me on 2345-67
// lalalalala -> tom's song...lalala
// hi i am PAUL you can call me on 12345-89
// hi i am SAM, i work at GOLANG INC. call me on 12-34-56
// hi i am MIKE you can call me on 123-123
