// Interfaces are named collections of method signatures(签名).

package main
import "fmt"
import "math"

type geometry interface {
    area() float64
    perim() float64
}
// Here's a basic interface for geometric(几何学的) shapes.

type rect struct {
    width, height float64
}

type circle struct {
    radius float64
}
// For our example we'll implement this interface on `rect` and
// `circle` types.

func (r rect) area() float64 {
    return r.width * r.height
}
func (r rect) perim() float64 {
    return 2*r.width + 2*r.height
}
// To implement an interface in Go, we just need to
// implement all the methods in the interface.
// Here we implement geometry on `rect`s.

func (c circle) area() float64 {
    return math.Pi * c.radius * c.radius
}
func (c circle) perim() float64 {
    return 2 * math.Pi * c.radius
}
// The implementation for `circle`s.

func measure(g geometry) {
    fmt.Println(g)
    fmt.Println(g.area())
    fmt.Println(g.perim())
}
// If a variable has an interface type, then we can call
// methods that are in the named interface. Here's a generic
// `measure` function taking advantage of this to work on any `geometry`.

func main() {
    r := rect{width: 3, height: 4}
    c := circle{radius: 5}

    measure(r)
    // {3 4}
    // 12
    // 14
    measure(c)
    // {5}
    // 78.53981633974483
    // 31.41592653589793
    /* The `circle` and `rect` struct types both implement the 
    `geometry interface so we can use interfaces of these structs as
    arguments to `measure`. */
}
