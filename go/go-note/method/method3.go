package main
import "fmt"

type User struct {
    id int
    name string
}

type Manager struct {
    User
}

func (self *User) ToString() string {   // receiver = &(Manager.User)
    return fmt.Sprintf("User: %p, %v", self, self)
}

func main() {
    m := Manager{User{1, "Tom"}}

    fmt.Printf("manager -> %p\n", &m)
    fmt.Println(m.ToString())
}
// manager -> 0xc42000a200
// User: 0xc42000a200, &{1 Tom}
