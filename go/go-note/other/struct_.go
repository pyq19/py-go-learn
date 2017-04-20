package main
import "fmt"

type user struct { // 结构体类型
    name string
    age byte
}

type manager struct {
    user            // 匿名嵌入其他类型
    title string
}

func main() {
    var m manager
    m.name = "Tom"  // 直接访问匿名字段的成员
    m.age = 29
    m.title = "CTO"

    fmt.Println(m)
}
// {{Tom 29} CTO}
