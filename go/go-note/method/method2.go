package main
import "fmt"


type Data struct {
    x int
}

func (self Data) ValueTest() {      // func ValueTest(self Data);
    fmt.Printf("Value .. %p\n", &self)
}

func (self *Data) PointerTest() {   // func PointerTest(self *Data);
    fmt.Printf("Pointer: %p\n", self)
}

func main() {
    d := Data{}
    p := &d
    fmt.Printf("Data -> %p\n", p)

    d.ValueTest()   // ValueTest(d)
    d.PointerTest() // PointerTest(&d(

    p.ValueTest()   // ValueTest(*p)
    p.PointerTest() // PointerTest(p)
}
// Data -> 0xc42000e250
// Value .. 0xc42000e260
// Pointer: 0xc42000e250
// Value .. 0xc42000e268
// Pointer: 0xc42000e250
