// Go's structs are typed collections of fields.
// They're useful for grouping data together to form records.

package main
import "fmt"

type person struct {
    name string
    age int
}
// This `person` struct type has `name` and `age` fields.

func main() {
    fmt.Println(person{"Bob", 20})
    // {Bob 20}
    // This syntax creates a new struct.

    fmt.Println(person{name: "Alice", age: 30})
    // {Alice 30}
    // You can name the fields when initializing a struct.

    fmt.Println(person{name: "Fred"})
    // {Fred 0}
    // Omitted fields will be zero-valued.

    fmt.Println(&person{name: "Ann", age:40})
    // &{Ann 40}
    // An & prefix yields a pointer to the struct.

    s := person{name: "Sean", age: 50}
    fmt.Println(s.name)
    // Sean
    // Access struct fields with a dot.

    sp := &s
    fmt.Println(sp.age)
    // 50
    // You can also use dots with struct pointers - 
    // the pointers are automatically dereferenced.

    sp.age = 51
    fmt.Println(sp.age)
    // 51
    // Structs are mutable(易变的,不定的).
}
