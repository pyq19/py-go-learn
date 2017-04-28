// http://stackoverflow.com/questions/22892120/how-to-generate-a-random-string-of-a-fixed-length-in-golang

// I want a random string of characters only (uppercase or lowercase), no numbers in Golang.
// What is the fastest and simplest way to do this in Go?

/////////////////
/*
// You can just write code for it. This code can be a little simpler if you want to rely on the letters
// all being single bytes when encoded in UTF-8.
package main
import (
    "fmt"
    "math/rand"
)
var letters = []rune("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

func randSeq(n int) string {
    b := make([]rune, n)
    for i := range b {
        b[i] = letters[rand.Intn(len(letters))]
    }
    return string(b)
}

func main() {
    fmt.Println(randSeq(10))
}
// XVlBzgbaiC
*/
//////////////////////////

