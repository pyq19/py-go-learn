package main
import "fmt"

func main() {
    type data struct{ a int }
    var d = data{1234}
    var p *data
    p = &d
    fmt.Printf("%p, %v\n", p, p.a) // 直接用指针访问目标对象成员，无需转化

}

// 0xc42007a050, 1234
