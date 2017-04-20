package main
// import "fmt"

func test() (int, string) {
    return 1, "abc"
}

func main() {
    _, s := test()
    println(s)
}
