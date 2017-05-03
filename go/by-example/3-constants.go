// Go supports constants(常数, 常量) of character, string, boolean and numeric values.

package main
import "fmt"
import "math"

const s string = "constant"

func main() {
    fmt.Println(s)// constant

    const n = 500000000
    // a `const` statement can appear anywhere a `var` statement can.

    const d = 3e20 / n
    fmt.Println(d)// 6e+11
    // Constant expressions perform arithmetic with arbitrary precision.
    // 常量表达式执行算法 任意的,武断的 精度

    fmt.Println(int64(d))// 600000000000
    // A numeric constant has no type until it's given one
    // such as by an explicit cast(投掷,计算).

    fmt.Println(math.Sin(n))// -0.28470407323754404
    // A number can be given a type by using it in a context 
    // that requires one, such as a variable assignment of function call.
    // e.g. here `math.Sin` expects a `float64`.
}





