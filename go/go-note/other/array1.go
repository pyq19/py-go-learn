package main
import "fmt"

func main() {
    type user struct {
        name string
        age byte
    }

    d := [...]user{
        {"Tom", 20},        // 省略了类型标签
        {"Mary", 18},
    }

    fmt.Printf("%#v\n", d)
}
// [2]main.user{
//    main.user{name:"Tom", age:0x14},
//    main.user{name:"Mary", age:0x12}
// }
