// channel

package main
import "fmt"

func sum(a []int, c chan int) {
    sum := 0
    for _, v := range a {
        sum += v
    }
    c <- sum                // send sum to c
}

/*
func main() {
    a := []int{7, 2, 8, -9, 4, 0}
    c := make(chan int)
    go sum(a[:len(a)/2], c)
    go sum(a[len(a)/2:], c)
    x, y := <-c, <-c        // receive from c

    fmt.Println(x, y, x + y)
}
// -5 17 12
*/

func main() {
    a := []int{7, 2, 8, -9, 4, 0}
    c1 := make(chan int)
    c2 := make(chan int)
    go sum(a[:len(a)/2], c1)
    go sum(a[len(a)/2:], c2)
    x, y := <-c1, <-c2        // receive from c

    fmt.Println(x, y, x + y)
}
// 17 -5 12
