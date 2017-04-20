package main

func main() {
    var t1, t2 interface{}
    println(t1==nil, t1==t2)
    t1, t2 = 100, 100
    println(t1==t2)

    t1, t2 = map[string]int{}, map[string]int{}
    println(t1==t2)
}
// true true
// true
// panic: runtime error: comparing uncomparable type map[string]int
