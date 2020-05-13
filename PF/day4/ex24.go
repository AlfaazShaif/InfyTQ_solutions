//PF-Exer-24
//This verification is based on string match.

package main

import ("fmt")
func main() {
    //Write your program logic here
    var result int;
    result = find_square(4)
    fmt.Println(result)
}

func find_square(num int) int {
    return num * num
}