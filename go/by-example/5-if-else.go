// Branching with `if` and `else` in Go is straight-forward.

package main
import "fmt"
func main() {
    if 7%2 == 0 {
        fmt.Println("7 is even")
    } else {
        fmt.Println("7 is odd")
    }
    // 7 is odd

    if 8%4 == 0 {
        fmt.Println("8 is divisible by 4")
    }
    // 8 is divisible by 4

    if num := 9; num < 0 {
        fmt.Println(num, "is negative")
    } else if num < 10 {
        fmt.Println(num, "has 1 digit")
    } else {
        fmt.Println(num, "has multiple digits")
    }
    // 9 has 1 digit
    // A statement can precede(优于,在之前) conditionals;
    // any variables declared in this statement are available in all branches.

}


