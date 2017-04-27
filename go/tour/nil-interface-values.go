package main
import "fmt"

type I interface {
    M()
}

func main() {
    var i I
    describe(i)
    i.M()
}

func describe(i I) {
    fmt.Printf("(%v, %T)\n", i, i)
}
// (<nil>, <nil>)
// panic: runtime error: invalid memory address or nil pointer dereference
// [signal SIGSEGV: segmentation violation code=0x1 addr=0x20 pc=0x1088afa]
// 
// goroutine 1 [running]:
// main.main()
//     /Users/Mccree/p/py-go-learn/go/tour/nil-interface-values.go:11 +0x3a
//     exit status 2
