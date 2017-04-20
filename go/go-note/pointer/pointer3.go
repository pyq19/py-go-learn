package main

func main() {
    x := 10
    p := &x
    p++         // 无效操作：p++ non-numeric type*int
    var p2*int = p + 1  // 无效操作: p+1  mismatched types*int and int

    p2 = &x
    println(p == p2)
}
// ./pointer3.go:6: invalid operation: p++ (non-numeric type *int)
// ./pointer3.go:7: invalid operation: p + 1 (mismatched types *int and int)
