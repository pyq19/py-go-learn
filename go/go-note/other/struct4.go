// struct 匿名字段

package main
import "fmt"

type Skills []string

type Human struct {
    name string
    age int
    weight int
}

type Student struct {
    Human           // 匿名字段 struct
    Skills          // 匿名字段 自定义的类型 string slice
    int             // 内置类型作为匿名字段
    speciality string
}

func main() {
    jane := Student{Human:Human{"Jane", 35, 100}, speciality:"Biology"}

    fmt.Println("her name is ->s", jane.name)
    fmt.Println("age ->", jane.age, "weight ->", jane.weight, "speciality->", jane.speciality)

    jane.Skills = []string{"anatomy"}               // 修改Skills 技能字段
    fmt.Println("her skills are", jane.Skills)
    fmt.Println("she acquired two new ones")
    jane.Skills = append(jane.Skills, "physics", "golang")
    fmt.Println("her skills now are ->", jane.Skills)

    jane.int = 3                                    // 修改匿名内置类型字符
    fmt.Println("her preferred number is ->", jane.int)
}
// her name is ->s Jane
// age -> 35 weight -> 100 speciality-> Biology
// her skills are [anatomy]
// she acquired two new ones
// her skills now are -> [anatomy physics golang]
// her preferred number is -> 3
