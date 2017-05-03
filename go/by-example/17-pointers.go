// Go supports pointers, allowing you to
// pass references(引用) to values and records within your program.

package main
import "fmt"
/* We'll show hou pointers work in contrast(对比) to values with 2 functions:
`zeroval` and `zeroptr`. */

func zeroval(ival int) {
    ival = 0
}
// `zeroval` has an int parameter, so arguments will be passed to it by value.
// `zeroval` will get a copy of `ival` distinct(明显的,有区别的) from the
// one in the calling function.

func zeroptr(iptr *int) {
    *iptr = 0
}
// `zeroptr` in contrast has an `*int` parameter, meaning that it takes an
// `int` pointer. The `*iptr` code in the function body
// then dereferences(重新引用？) the pointer from its memory address
// to the current value at that address.
// Assigning a value to dereferenced pointer changes the value at the
// referenced address.

func main() {
    i := 1
    fmt.Println("initial:", i)// initial: 1

    zeroval(i)
    fmt.Println("zeroval:", i)// zeroval: 1

    zeroptr(&i)
    fmt.Println("zeroptr:", i)// zeroptr: 0
    // The &i syntax gives the memory address of `i`, 
    // i.e. a pointer to `i`. (i.e. that is to say ... 这就是说)

    fmt.Println("pointer:", &i)// pointer: 0xc42000e250
    // Pointers can be printed too.
}
// `zeroval` doesn't change the `i` in main,
// but `zeroptr` does because it has a reference to the memory address
// for that variable.
