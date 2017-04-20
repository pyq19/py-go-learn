package main
import "fmt"

// method value 会复制 receiver


type User struct {
    id int
    name string
}

func (self User) Test() {
    fmt.Println(self)
}

func main() {
    u := User{1, "Tom.."}
    mValue := u.Test        //立即复制 receiver 因为不是指针类型，不受后续修改影响

    u.id, u.name = 2, "Jack...."
    u.Test()

    mValue()
}
// {2 Jack....}
// {1 Tom..}
