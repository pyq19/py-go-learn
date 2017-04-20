// 如何创建goroutine 以及goroutine 调度器的行为
package main
import (
    "fmt"
    "runtime"
    "sync"
)

func main() {
    runtime.GOMAXPROCS(2)

    var wg sync.WaitGroup
    wg.Add(2)

    fmt.Println("start goroutines..")

    go func() {
        defer wg.Done()

        for count := 0; count < 3; count++ {
            for char := 'a'; char < 'a'+26; char++ {
                fmt.Printf("%c ", char)
            }
        }
    }()

    go func() {
        defer wg.Done()
        for count := 0; count < 3; count++ {
            for char := 'A'; char < 'A'+26; char++ {
                fmt.Printf("%c ", char)
            }
        }
    }()

    fmt.Println("waiting to finish")
    wg.Wait()

    fmt.Println("\nTerminating program....")
}
// start goroutines..
// waiting to finish
// A B C D E F G H I J K L M N O a P Q b R c S d T e U V f W g X h Y i Z j A k B l C m D n E o F p G q H r I s J t K u v w x y z a L b c d e f M g N h O i P j Q k R l S m T n U o V p W q X r Y s Z t A u B v C w D x E y F z G a H b I c J d K e L f M g N h O i P j Q k R l S m T n U o V p W q X r Y s Z t u v w x y z
// Terminating program....
