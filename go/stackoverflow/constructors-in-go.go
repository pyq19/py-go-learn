// http://stackoverflow.com/questions/18125625/constructors-in-go
// Constructors in Go

// I have a struct and I would like it to be initialised with some sensible default values.

// Typically, the thing to do here is to use a constructor but since go isn't really OOP in the traditional 
// sense these aren't true objects and it has no constructors.

// I have noticed the init method but that is at the package level.
// Is there something else similar that can be used at the struct level?

// If not what is the accepted best practice for this type of thing in Go?

//////////////////////
/*
// There are some equivalents of constructors for when the zero values can't make sensible
// default values or for when some parameter is necessary for the struct initialization.

// Supposing you have a struct like this:
type Thing struct {
    Name string
    Num  int
}
// then, if the zero values aren't fitting, you would typically construct an instance with a `NewThing`
// function returning a pointer:
func NewThing(someParameter string) *Thing {
    p := new(Thing)
    p.Name = someParameter
    p.Num = 33  // <- a very sensible default value
    return p
}
// When your struct is simple enough, you can use this condensed construct:
func NewThing(someParameter string) *Thing {
    return &Thing{someParameter, 33}
}
// If you don't want to return a pointer, then a practice is to call the function `makeThing` instead of `NewThing`:
func makeThing(name string) Thing {
    return Thing{name, 33}
}
*/
/////////////////////
/*
// Go has objects. Objects can have constructors (although not automatic constructors).
// And finally, Go is an OOP language (data types have methods attached, but admittedly there are endless 
// definitions of what OOP is.)

// Nevertheless, the accepted best practice is to write zero or more constructors for your types.

func NewThing(someParameter string) *Thing {
    return &Thing{someParameter, 33} // <- 33: a very sensible default value
}

// The reason I want to show you this version is that pretty often "inline" literals can be used instead 
// of a "constructor" call.
a := NewThing("foo")
b := &Thing{"foo", 33}

// Now *a == *b
*/
/////////////////////

// There are no default constructors in Go, but you can declare methods for any type.
// You could make it a habit to declare a method called "Init".
// Not sure if how this relates to best practices,
// but it helps keep names short without loosing clarity.
package main
import "fmt"
type Thing struct {
    Name string
    Num int
}
func (t *Thing) Init(name string, num int) {
    t.Name = name
    t.Num = num
}
func main() {
    t := new(Thing)
    t.Init("Hello", 5)
    fmt.Printf("%s: %d\n", t.Name, t.Num)
}
// Hello: 5
///////////////////////

