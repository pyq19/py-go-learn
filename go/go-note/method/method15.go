// 使用method 而不是单纯的函数

package main
import (
    "fmt"
    "math"
)

type Rectangle struct {
    width, height float64
}

type Circle struct {
    radius float64
}

func (r Rectangle) area() float64 {
    return r.width * r.height
}

func (c Circle) area() float64 {
    return c.radius * c.radius * math.Pi
}

func main() {
    r1 := Rectangle{12, 2}
    r2 := Rectangle{2, 6}
    c1 := Circle{10}
    c2 := Circle{25}

    fmt.Println("area of r1 ->", r1.area())
    fmt.Println("area of r2 ->", r2.area())
    fmt.Println("area of c1 ->", c1.area())
    fmt.Println("area of c2 ->", c2.area())
}
// area of r1 -> 24
// area of r2 -> 12
// area of c1 -> 314.1592653589793
// area of c2 -> 1963.4954084936207
