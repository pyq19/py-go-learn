// http://stackoverflow.com/questions/2032149/optional-parameters

// Can Go have optional parameters? Or can I just define two functions with the same name and a different number of arguments?

///////////

// You can use a struct which includes the parameters:
/*
package main

type Params struct {
    a, b, c int
}

func doIt(p Params) int {
    return p.a + p.b + p.c
}

func main() {
    println(doIt(Params{a: 1, c: 9})) // 10
}
*/
///////////

package main
func foo(params ...int) {
    println(len(params))
}
func main() {
    foo()
    foo(1)
    foo(1, 2, 3)
}
// 0
// 1
// 3
