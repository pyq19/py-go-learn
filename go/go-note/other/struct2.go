package main
import "fmt"

type person struct {
    name string
    age int
}

func Older(p1, p2 person) (person, int) {
    if p1.age > p2.age {
        return p1, p1.age - p2.age
    }
    return p2, p2.age - p1.age
}

func main() {
    var tom person
    tom.name, tom.age = "TOM", 18           // 赋值初始化

    bob := person{age:25, name:"BOB"}      // 两个字段都写清楚的初始化

    paul := person{"PAUL", 30}              // 按照struct 定义顺序初始化

    tb_Older, tb_diff := Older(tom, bob)
    tp_Older, tp_diff := Older(tom, paul)
    bp_Older, bp_diff := Older(bob, paul)

    fmt.Printf("Of %s and %s, %s is older by %d years..\n", tom.name, bob.name, tb_Older.name, tb_diff)
    fmt.Printf("Of %s and %s, %s is older by %d years..\n", tom.name, paul.name, tp_Older.name, tp_diff)
    fmt.Printf("Of %s and %s, %s is older by %d years..\n", bob.name, paul.name, bp_Older.name, bp_diff)
}
// Of TOM and BOB, BOB is older by 7 years..
// Of TOM and PAUL, PAUL is older by 12 years..
// Of BOB and PAUL, PAUL is older by 5 years..
