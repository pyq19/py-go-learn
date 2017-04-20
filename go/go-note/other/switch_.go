package main

/*
func main() {
    x := []int{1, 2, 3}
    i := 2

    switch i {
        case x[1]:
            println("a")
        case 1, 3:
            println("B")
        default:
            println("c")
    }
}
// a
*/

/*
// fallthrough 可继续下一分支，但不再判断条件
func main() {
    x := 10
    switch x {
        case 10:
            println("a")
            fallthrough
        case 0:
            println("b")
    }
}
// a
// b
*/

/*
// 省略条件表达式，可当if...else   if...else... 使用
func main() {
    x := []int{1, 2, 3}
    switch {
        case x[1] > 0:
            println("a")
        case x[1] < 0:
            println("b")
        default:
            println("c")
    }

    switch i := x[2]; {            // 带初始化语句
        case i > 0:
            println("a")
        case i < 0:
            println("b")
        default:
            println("c")
    }
}
// a
// a
*/


