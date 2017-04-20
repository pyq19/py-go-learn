package main
import "fmt"
import "unsafe"

func main() {
    var a, b chan int = make(chan int, 3), make(chan int)
    var c chan bool

    println(a==b)
    println(c==nil)

    fmt.Printf("%p, %d\n", a, unsafe.Sizeof(a))
}
// false
// true
// 0xc420070000, 8
