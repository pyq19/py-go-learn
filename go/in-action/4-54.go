package main
import "fmt"

func main() {
    colors := map[string]string{
        "blue":     "#123",
        "red":      "#234",
        "yellow":   "#345",
    }

    for key, value := range colors {
        fmt.Printf("key->%s value->%s\n", key, value)
    }

    removeColor(colors, "blue")

    for key, value := range colors {
        fmt.Printf("key->%s value->%s\n", key, value)
    }

}

func removeColor(colors map[string]string, key string) {
    delete(colors, key)
}
// key->blue value->#123
// key->red value->#234
// key->yellow value->#345
// key->red value->#234
// key->yellow value->#345
