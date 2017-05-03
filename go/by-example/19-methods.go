// Go supports methods defined on struct types.

package main
import "fmt"

type rect struct {
    width, height int
}
func (r *rect) area() int {
    return r.width * r.height
}
// This area method has a receiver type of *rect.

func (r rect) perim() int {
    return 2*r.width + 2*r.height
}
// Methods can be defined for either pointer or value receiver
// types. Here's an example of a value receiver.

func main() {
    r := rect{width: 10, height: 5}

    fmt.Println("area: ", r.area())
    // area:  50
    // Here we call the 2 methods defined for our struct.

    fmt.Println("perim:", r.perim())
    // perim: 30

    rp := &r
    fmt.Println("area: ", rp.area())
    // area:  50
    fmt.Println("perim:", rp.perim())
    // perim: 30
    /* Go automatically handles conversion between values and
    pointers for method calls. You may want to use a pointer
    receiver type to avoid copying on method calls or to allow
    the method to mutate(变化,改变) the receiving struct. */
}
