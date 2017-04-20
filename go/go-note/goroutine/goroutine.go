package main
//import "fmt"
import "sync"
import "math"

func sum(id int) {
    var x int64
    for i := 0; i < math.MaxUint32; i++ {
        x += int64(i)
    }
    println(id, x)
}

func main() {
    wg := new(sync.WaitGroup)
    wg.Add(2)

    for i := 0; i < 2; i++ {
        go func(id int) {
            defer wg.Done()
            sum(id)
        }(i)
    }
    wg.Wait()
}
// 0 9223372030412324865
// 1 9223372030412324865
