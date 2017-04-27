package main

import (
    "fmt"
    "runtime"
)

func main() {
    fmt.Print("Go runs on ")
    switch os := runtime.GOOS; os {
    case "darwin":
        fmt.Println("os x.")
    case "linux":
        fmt.Println("linux..")
    default:
        fmt.Printf("%s", os)
    }
}
