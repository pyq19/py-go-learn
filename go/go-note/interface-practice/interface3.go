package main

import "fmt"

type Tester struct {
    s interface {
        String() string
    }
}

type User struct {
    id  int
    name    string
}

func (self *User) String() string {
    return fmt.Sprintf("user %d, %s", self.id, self.name)
}

func main() {
    t := Tester{&User{1, "TOM"}}
    fmt.Println(t.s.String())
}
// user 1, TOM
