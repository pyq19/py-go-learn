// struct 匿名字段

package main
import "fmt"

type Human struct {
    name string
    age int
    weight int
}

type Student struct {
    Human       // 匿名字段，默认Student 包含Human 所有字段
    speciality string
}

func main() {
    mark := Student{Human{"Mark", 25, 120}, "computer science"}
    fmt.Println("his name ->", mark.name)
    fmt.Println("age ->", mark.age)
    fmt.Println("weight ->", mark.weight)
    fmt.Println("speciality ->", mark.speciality)

    mark.speciality = "AI~~~"
    fmt.Println("mark changed his speciality ....")
    fmt.Println("mark new speciality ->", mark.speciality)

    fmt.Println("mark become old")
    mark.age = 80
    fmt.Println("mark age is ->", mark.age)
}
// his name -> Mark
// age -> 25
// weight -> 120
// speciality -> computer science
// mark changed his speciality ....
// mark new speciality -> AI~~~
// mark become old
// mark age is -> 80
