package main
import "fmt"

type Human struct {
    name string
    age int
    phone string            // Human 类型拥有的字段
}

type Employee struct {
    Human                   // 匿名字段
    speciality string
    phone string            // 雇员的phone 字段
}

func main() {
    Bob := Employee{Human{"Bob", 12, "136*********"}, "java", "1377878****"}
    fmt.Println("Bob's work phone is ->", Bob.phone)

    // 如果访问Human 里的phone 字段
    fmt.Println("Bob's personal phone is ->", Bob.Human.phone)
}
// Bob's work phone is -> 1377878****
// Bob's personal phone is -> 136*********
