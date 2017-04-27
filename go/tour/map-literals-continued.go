package main
import "fmt"

type Vertex struct {
    Lab, Long float64
}

var m = map[string]Vertex{
    "Bell Labs": {40.000, -11.222},
    "Google": {12.34, 67.89},
}

func main() {
    fmt.Println(m)// map[Bell Labs:{40 -11.222} Google:{12.34 67.89}]
}
