package main

import "fmt"

func main() {
    q := []int{1, 3, 5, 7, 9, 11}
    fmt.Println(q)

    r := []bool{true, false, true, true, false, true}
    fmt.Println(r)

    s := []struct {
        i int
        b bool
    }{
        {2, true},
        {3, false},
        {4, true},
        {5, false},
        {6, true},
        {7, false},
    }

    fmt.Println(s)
}

/*
[1 3 5 7 9 11]
[true false true true false true]
[{2 true} {3 false} {4 true} {5 false} {6 true} {7 false}]
*/
